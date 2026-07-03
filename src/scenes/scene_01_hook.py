"""
[00:00 - 00:35] SCENE 1: HOOK (REVISI)
Perbaikan dari versi asli:
1. Bug streaming: FadeIn(ai_lines) di awal membuat semua kata langsung
   opacity=1 sebelum loop per-kata jalan, jadi efek "kata demi kata" tidak
   pernah kelihatan. Fix: mobject di-add ke scene dalam kondisi invisible
   (set_opacity(0)) tanpa animasi, baru loop FadeIn per kata yang benar-benar
   memunculkannya satu-satu.
2. Bug index highlight: ai_words[8:12] menunjuk ke kata yang salah
   ("awal. Dia hanya sangat", bukan "menebak satu kata berikutnya.").
   Fix: cari index frasa target dengan pencocokan teks, bukan angka mentah,
   supaya kalau response_text diedit nanti, highlight otomatis ikut benar
   (atau langsung error jelas kalau frasa tidak ditemukan, bukan salah diam-diam).
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from manim import *
from src.constants import *
from src.components.chat_ui import ChatGPTUI
from src.utils.animations import TypewriterText, create_glowing_surround_rect


def find_phrase_index(full_text: str, phrase: str) -> int:
    """
    Cari index kata awal dari sebuah frasa di dalam teks penuh,
    berdasarkan pencocokan kata per kata (bukan posisi angka manual).
    Raise ValueError kalau frasa tidak ditemukan, biar salah ketik
    langsung ketahuan saat development, bukan salah diam-diam saat render.
    """
    words = full_text.split()
    target = phrase.split()
    n = len(target)
    for i in range(len(words) - n + 1):
        if words[i:i + n] == target:
            return i
    raise ValueError(
        f"Frasa '{phrase}' tidak ditemukan di dalam response_text. "
        f"Cek ejaan atau tanda baca (mis. titik di akhir kata)."
    )


class HookScene(Scene):
    def construct(self):
        self.camera.background_color = DARK_BG

        # 1. Munculkan Antarmuka ChatGPT Mockup
        chat_ui = ChatGPTUI(width=11.0, height=6.5)
        self.play(FadeIn(chat_ui, scale=0.9), run_time=TIME_NORMAL)
        self.wait(0.5)

        # 2. Cursor mengetik pertanyaan user
        prompt_bubble = chat_ui.create_user_prompt("Apa itu ChatGPT dan bagaimana cara kerjanya?")
        self.play(FadeIn(prompt_bubble, shift=UP * 0.3), run_time=TIME_NORMAL)
        self.wait(0.5)

        # 3. Siapkan teks jawaban AI
        response_text = (
            "ChatGPT sebenarnya tidak pernah tahu jawaban penuh dari awal. "
            "Dia hanya sangat jago menebak satu kata berikutnya. "
            "Terus, satu kata lagi. Terus, satu kata lagi. Berulang-ulang secepat kilat!"
        )
        ai_words, ai_lines = chat_ui.create_ai_response_words(response_text)

        # FIX BUG #1: tambahkan ke scene dalam kondisi tak terlihat, TANPA animasi
        # fade massal. Posisi sudah benar (hasil layout dari create_ai_response_words),
        # tinggal opacity-nya yang kita kontrol manual lewat loop di bawah.
        ai_lines.set_opacity(0)
        self.add(ai_lines)

        # Animasi streaming kata-per-kata yang sesungguhnya
        for word in ai_words:
            self.play(FadeIn(word, shift=UP * 0.1), run_time=0.08)

        self.wait(1.0)

        # FIX BUG #2: cari frasa target lewat pencocokan teks, bukan index manual
        start_idx = find_phrase_index(response_text, "menebak satu kata berikutnya.")
        phrase_len = len("menebak satu kata berikutnya.".split())
        target_phrase = VGroup(*ai_words[start_idx:start_idx + phrase_len])

        glow_rect = create_glowing_surround_rect(target_phrase, color=YELLOW_3B1B, buff=0.1)
        self.play(Create(glow_rect), run_time=TIME_NORMAL)

        highlight_text = Text(
            "FOKUS TUNGGAL: Menebak Satu Kata Berikutnya!",
            font=FONT_PRIMARY,
            font_size=FONT_SIZE_BODY,
            color=YELLOW_3B1B
        ).to_edge(UP, buff=0.4)

        # CATATAN: posisi ini berpotensi nabrak header chat_ui kalau frame
        # terlalu sempit. Cek hasil render — kalau mepet, ganti jadi:
        # highlight_text.next_to(chat_ui, UP, buff=0.3)
        self.play(Write(highlight_text), run_time=TIME_NORMAL)
        self.wait(TIME_READING)

        # 5. Transisi keluar untuk persiapan scene berikutnya
        self.play(
            FadeOut(glow_rect),
            FadeOut(chat_ui),
            FadeOut(highlight_text),
            run_time=TIME_NORMAL
        )

if __name__ == "__main__":
    with tempconfig({"quality": "high_quality", "preview": True}):
        scene = HookScene()
        scene.render()