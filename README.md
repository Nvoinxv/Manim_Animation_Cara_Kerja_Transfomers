# Proyek Animasi Manim: Cara Kerja Transformers (3Blue1Brown Style)

Selamat datang di repositori proyek animasi **Manim** untuk video edukasi AI berdurasi 10 menit:
> **"Kenapa ChatGPT Bisa Ngobrol Kaya Manusia? (Bukan Sihir, Ini Matematika)"**

Proyek ini dirancang dengan standar arsitektur profesional, modular, dan siap produksi. Gaya visual (aesthetics) mengadopsi filosofi desain **3Blue1Brown (Grant Sanderson)** — berfokus pada keanggunan geometris, pergerakan matematika yang halus, representasi vektor yang intuitif, serta palet warna yang harmonis pada latar belakang gelap.

---

## 📁 Struktur Folder & Arsitektur Proyek

```text
Projek_Video_Cara_Kerja_Transfomers_10_Menit/
├── assets/                     # Aset multimedia eksternal
│   ├── audio/                  # Voiceover (VO) per scene & background music
│   ├── fonts/                  # Custom fonts (e.g., Inter, CMU Serif / LaTeX)
│   ├── images/                 # Gambar, ikon SVG (ikon otak, logo, dll.)
│   └── README.md               # Panduan pengelolaan aset
├── scripts/                    # Skrip utilitas & otomatisasi render
│   └── render_all.py           # CLI runner untuk render & stitching video otomatis
├── src/                        # Source code utama (Modular Architecture)
│   ├── __init__.py
│   ├── constants.py            # Palet warna 3B1B, timing standar, resolusi & tipografi
│   ├── components/             # Komponen visual modular & reusable
│   │   ├── __init__.py
│   │   ├── chat_ui.py          # Mockup antarmuka ChatGPT & animasi typewriter
│   │   ├── word_embedder.py    # Ruang vektor 2D/3D, token cluster & jarak semantik
│   │   ├── attention_net.py    # Heatmap koneksi attention, lampu sorot multi-head
│   │   └── layer_stack.py      # Layer berlapis transparan (hierarchical abstraction)
│   ├── scenes/                 # Skrip scene animasi (1-to-1 dengan skrip video)
│   │   ├── __init__.py
│   │   ├── scene_01_hook.py        # [00:00 - 00:35] Hook: Real-time Word Prediction
│   │   ├── scene_02_reframe.py     # [00:35 - 01:30] Reframe: Mesin Prediksi & Probabilitas
│   │   ├── scene_03_embedding.py   # [01:30 - 02:45] Langkah 1: Token & Embedding Space
│   │   ├── scene_04_attention.py   # [02:45 - 05:00] Langkah 2: Attention Mechanism (Klimaks)
│   │   ├── scene_05_layers.py      # [05:00 - 06:15] Langkah 3: Layered Processing
│   │   ├── scene_06_training.py    # [06:15 - 07:00] Sekilas Training & Data Masif
│   │   ├── scene_07_thinking.py    # [07:00 - 08:00] Apakah Dia Beneran "Mikir"? (Brain vs Stat)
│   │   └── scene_08_outro.py       # [08:00 - 08:45] Penutup & Call to Action
│   └── utils/                  # Fungsi bantu & custom animations
│       ├── __init__.py
│       ├── animations.py       # Custom Manim animations (Pulse, Glow, Stream)
│       └── layouts.py          # Pengatur tata letak grid, kurva probabilitas, axes
├── manim.cfg                   # Konfigurasi global Manim (60fps, 1080p, dark theme)
├── pyproject.toml              # Konfigurasi proyek Python modern
├── requirements.txt            # Daftar dependensi Python
└── README.md                   # Dokumentasi proyek (file ini)
```

---

## 🎯 Peta Waktu (Timestamp) & Pemetaan Scene

| Timestamp | Nama Scene di Skrip | File Scene (`src/scenes/`) | Fokus Visual (3Blue1Brown Style) |
| :--- | :--- | :--- | :--- |
| **00:00 - 00:35** | **HOOK** | `scene_01_hook.py` (`HookScene`) | Cursor ngetik, streaming teks real-time, highlight nebak satu kata berikutnya. |
| **00:35 - 01:30** | **REFRAME** | `scene_02_reframe.py` (`NextWordPredictionScene`) | Kalimat blank, kandidat kata melayang dengan bar probabilitas (Jakarta vs Kucing). |
| **01:30 - 02:45** | **LANGKAH 1** | `scene_03_embedding.py` (`TokenAndEmbeddingScene`) | Kata pecah jadi token, transformasi ke ruang koordinat 3D/2D (clustering semantik). |
| **02:45 - 05:00** | **LANGKAH 2 (KLIMAKS)** | `scene_04_attention.py` (`AttentionMechanismScene`) | *"Kucing itu tidur... karena **dia** capek"*. Garis panah berbobot (heatmap), multi-head spotlight. |
| **05:00 - 06:15** | **LANGKAH 3** | `scene_05_layers.py` (`LayerProcessingScene`) | Tumpukan layer transparan 3D, transformasi titik dari sintaksis ke abstrak. |
| **06:15 - 07:00** | **TRAINING** | `scene_06_training.py` (`TrainingOverviewScene`) | Jutaan dokumen disedot model, koreksi error iteratif, jaringan makin terstruktur. |
| **07:00 - 08:00** | **MIKIR VS STATISTIK**| `scene_07_thinking.py` (`ThinkingVsStatScene`) | Split screen: Otak biologis (neuron) vs Jaringan koordinat angka + konsep halusinasi. |
| **08:00 - 08:45** | **PENUTUP** | `scene_08_outro.py` (`OutroScene`) | Zoom out ke seluruh jaringan raksasa, teks kesimpulan geometris, CTA. |

---

## 🛠️ Cara Instalasi & Persiapan Lingkungan

### 1. Prasyarat Sistem
Pastikan sistem operasi Anda (Windows) sudah terinstal:
- **Python** 3.10 atau lebih baru.
- **FFmpeg** (Wajib untuk rendering video dan penggabungan klip di Manim).
- **LaTeX** (Opsional, Disarankan menggunakan MiKTeX atau TeX Live untuk render rumus matematika TeX/MathTex yang sempurna).

### 2. Setup Python Virtual Environment (`myenv`) & Instalasi Manim
Agar instalasi library **Manim** rapi dan tidak terbentur dengan library Python global di PC Anda, sangat disarankan menggunakan **Virtual Environment (`myenv`)**.

#### Cara Otomatis (Menggunakan Skrip Helper):
- **Windows PowerShell**: Jalankan `.\setup_env.ps1`
- **Git Bash / Linux / macOS**: Jalankan `bash setup_env.sh`

#### Cara Manual (Langkah demi Langkah):

1. **Buat Virtual Environment bernama `myenv`**:
   ```powershell
   python -m venv myenv
   ```

2. **Aktifkan Virtual Environment (`myenv`)**:
   - Jika Anda menggunakan **Git Bash / Linux / macOS**:
     ```bash
     source myenv/bin/activate
     ```
   - Jika Anda menggunakan **Windows PowerShell**:
     ```powershell
     .\myenv\Scripts\activate
     ```
   - Jika Anda menggunakan **Windows Command Prompt (CMD)**:
     ```cmd
     myenv\Scripts\activate.bat
     ```
   *(Setelah aktif, akan muncul tulisan `(myenv)` di awal baris terminal Anda).*

3. **Instal Manim & Seluruh Dependensi**:
   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

### 3. Keamanan File (`.gitignore`)
Proyek ini sudah dilengkapi dengan file `.gitignore` komprehensif yang otomatis melindungi dan memfilter:
- **Folder Environment (`myenv/`, `venv/`)**: Agar puluhan megabyte library tidak ikut ter-push ke Git.
- **File Sensitif (`.env`, `secrets.json`, API keys)**: Mencegah kebocoran kredensial atau rahasia pribadi.
- **Output Render Manim (`media/`, `*.mp4`)**: Mencegah video berukuran raksasa memenuhi repositori Git Anda (kecuali file aset SVG/gambar di `assets/images/`).

---

## 🚀 Cara Mengerjakan & Merender Video

Proyek ini dilengkapi dengan skrip otomatisasi `scripts/render_all.py` untuk mempermudah render satu per satu maupun sekaligus.

### 1. Merender Satu Scene Khusus (Untuk Preview / Iterasi)
Gunakan perintah `manim` langsung atau lewat skrip runner:
```powershell
# Preview kualitas rendah (cepat, 480p 15fps) - ideal untuk cek animasi
manim -pql src/scenes/scene_04_attention.py AttentionMechanismScene

# Preview kualitas tinggi (1080p 60fps) - siap produksi
manim -pqh src/scenes/scene_04_attention.py AttentionMechanismScene
```

### 2. Merender Seluruh Scene Menggunakan Skrip Runner
Skrip `scripts/render_all.py` akan merender seluruh 8 scene secara urut sesuai timeline video:

```powershell
# Render semua scene kualitas rendah (untuk draft preview)
python scripts/render_all.py --quality l

# Render semua scene kualitas tinggi (1080p 60fps)
python scripts/render_all.py --quality h

# Render dan langsung gabungkan (stitch) menjadi 1 video utuh MP4
python scripts/render_all.py --quality h --stitch --output final_video_transformers.mp4
```

---

## 🎨 Filosofi Desain & Panduan Visual (3B1B Style)

1. **Palet Warna Terukur**: Jangan gunakan warna primer RGB kasar. Gunakan konstanta dari `src/constants.py` (seperti `BLUE_3B1B`, `YELLOW_3B1B`, `TEAL_3B1B`, `DARK_BG`).
2. **Pergerakan Halus (Smooth Transitions)**: Hindari kemunculan objek yang tiba-tiba (`FadeIn` lebih baik daripada langsung muncul, gunakan `smooth` atau `exponential_decay` untuk `rate_func`).
3. **Fokus pada Klimaks (Scene 4 - Attention)**: Sesuai catatan skrip, durasi visual terlama dan paling detail dialokasikan pada mekanisme **Attention**. Garis koneksi harus merepresentasikan *attention weights* secara visual dengan ketebalan (`stroke_width`) dan opasitas (`stroke_opacity`) yang proporsional.
4. **Modularitas Komponen**: Jika Anda membuat elemen visual baru yang berpotensi dipakai berulang (misal: kotak token, node vektor), masukkan ke dalam `src/components/`.

---
*Dibuat untuk edukasi AI Indonesia. Selamat berkarya dan menciptakan video animasi kelas dunia!* 🚀
