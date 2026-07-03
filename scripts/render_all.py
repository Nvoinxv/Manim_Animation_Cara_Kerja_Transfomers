#!/usr/bin/env python
"""
Skrip Utilitas Runner: render_all.py
------------------------------------
Digunakan untuk merender satu atau seluruh scene Manim secara otomatis sesuai urutan skrip video,
serta menyediakan opsi penggabungan (stitching) klip video menjadi satu file MP4 utuh menggunakan FFmpeg.

Contoh Penggunaan:
    python scripts/render_all.py --quality l               # Preview cepat semua scene (480p 15fps)
    python scripts/render_all.py --quality h               # Render kualitas produksi (1080p 60fps)
    python scripts/render_all.py -q h --stitch             # Render dan gabungkan video
    python scripts/render_all.py --scene AttentionMechanismScene -q h # Render 1 scene khusus
"""

import argparse
import subprocess
import sys
import os
from pathlib import Path

# Daftar urutan scene sesuai timeline skrip video
SCENE_LIST = [
    ("src/scenes/scene_01_hook.py", "HookScene"),
    ("src/scenes/scene_02_reframe.py", "NextWordPredictionScene"),
    ("src/scenes/scene_03_embedding.py", "TokenAndEmbeddingScene"),
    ("src/scenes/scene_04_attention.py", "AttentionMechanismScene"),
    ("src/scenes/scene_05_layers.py", "LayerProcessingScene"),
    ("src/scenes/scene_06_training.py", "TrainingOverviewScene"),
    ("src/scenes/scene_07_thinking.py", "ThinkingVsStatScene"),
    ("src/scenes/scene_08_outro.py", "OutroScene"),
]

def parse_args():
    parser = argparse.ArgumentParser(description="Otomatisasi Render Proyek Manim Transformers")
    parser.add_argument(
        "-q", "--quality",
        choices=["l", "m", "h", "k"],
        default="l",
        help="Kualitas render: l (480p 15fps), m (720p 30fps), h (1080p 60fps), k (4K 60fps). Default: l"
    )
    parser.add_argument(
        "-s", "--scene",
        type=str,
        default=None,
        help="Nama kelas scene tertentu yang ingin dirender (misal: AttentionMechanismScene). Jika kosong, merender semua."
    )
    parser.add_argument(
        "--stitch",
        action="store_true",
        help="Gabungkan seluruh video hasil render menjadi satu file MP4 menggunakan FFmpeg."
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="final_video_transformers_10_menit.mp4",
        help="Nama file video akhir jika menggunakan opsi --stitch."
    )
    return parser.parse_args()

def render_scene(file_path: str, scene_name: str, quality: str):
    """
    Menjalankan perintah subproses Manim untuk merender satu scene.
    """
    cmd = ["manim", f"-pq{quality}", file_path, scene_name]
    print(f"\n🎬 [RENDERING] Memulai render: {scene_name} ({file_path}) dengan kualitas '{quality}'...")
    print(f"👉 Perintah: {' '.join(cmd)}")
    
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print(f"❌ [ERROR] Gagal merender scene: {scene_name}")
        return False
    print(f"✅ [SUKSES] Berhasil merender: {scene_name}")
    return True

def stitch_videos(quality: str, output_filename: str):
    """
    Menggabungkan klip video MP4 dari direktori media menggunakan FFmpeg concat demuxer.
    """
    print("\n🔗 [STITCHING] Mencari file hasil render untuk digabungkan...")
    
    # Menentukan direktori resolusi berdasarkan kualitas
    res_map = {"l": "480p15", "m": "720p30", "h": "1080p60", "k": "2160p60"}
    res_dir = res_map.get(quality, "480p15")
    
    video_files = []
    media_base = Path("media/videos")
    
    for file_path, scene_name in SCENE_LIST:
        scene_file_base = Path(file_path).stem
        clip_path = media_base / scene_file_base / res_dir / f"{scene_name}.mp4"
        if clip_path.exists():
            video_files.append(str(clip_path.resolve()))
        else:
            print(f"⚠️ [PERINGATAN] File klip tidak ditemukan: {clip_path}")
            
    if not video_files:
        print("❌ [ERROR] Tidak ada file klip video yang ditemukan untuk digabungkan!")
        return
        
    # Buat file daftar concat untuk FFmpeg
    concat_list_path = Path("concat_list.txt")
    with open(concat_list_path, "w", encoding="utf-8") as f:
        for vf in video_files:
            # Gunakan format file path aman untuk FFmpeg
            safe_path = vf.replace("\\", "/")
            f.write(f"file '{safe_path}'\n")
            
    print(f"📋 Daftar klip yang akan digabung:\n" + "\n".join([f"  - {vf}" for vf in video_files]))
    
    # Jalankan perintah FFmpeg
    output_path = Path(output_filename).resolve()
    ffmpeg_cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", str(concat_list_path),
        "-c", "copy", str(output_path)
    ]
    
    print(f"\n🚀 Menjalankan FFmpeg: {' '.join(ffmpeg_cmd)}")
    res = subprocess.run(ffmpeg_cmd)
    
    # Hapus file temporary concat
    if concat_list_path.exists():
        concat_list_path.unlink()
        
    if res.returncode == 0:
        print(f"\n🎉 [SELESAI] Video akhir berhasil dibuat di: {output_path}")
    else:
        print("\n❌ [ERROR] Gagal menggabungkan video dengan FFmpeg.")

def main():
    args = parse_args()
    
    # Pastikan berada di root direktori proyek
    project_root = Path(__file__).resolve().parent.parent
    os.chdir(project_root)
    print(f"📂 Root Direktori Kerja: {project_root}")
    
    # Jika user meminta render 1 scene khusus
    if args.scene:
        found = False
        for file_path, scene_name in SCENE_LIST:
            if scene_name.lower() == args.scene.lower():
                render_scene(file_path, scene_name, args.quality)
                found = True
                break
        if not found:
            print(f"❌ [ERROR] Scene dengan nama '{args.scene}' tidak ditemukan di daftar SCENE_LIST!")
        return
        
    # Render semua scene secara urut
    print(f"🎬 Memulai proses render untuk {len(SCENE_LIST)} scene...")
    success_count = 0
    for file_path, scene_name in SCENE_LIST:
        if render_scene(file_path, scene_name, args.quality):
            success_count += 1
        else:
            print(f"⚠️ Proses render dihentikan karena kesalahan pada {scene_name}.")
            break
            
    print(f"\n📊 Selesai merender {success_count} dari {len(SCENE_LIST)} scene.")
    
    # Jika opsi --stitch diaktifkan dan semua scene berhasil
    if args.stitch and success_count == len(SCENE_LIST):
        stitch_videos(args.quality, args.output)
    elif args.stitch:
        print("⚠️ [PERINGATAN] Penggabungan (stitching) dibatalkan karena ada scene yang gagal dirender.")

if __name__ == "__main__":
    main()
