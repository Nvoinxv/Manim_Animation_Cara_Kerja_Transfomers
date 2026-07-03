# Panduan Pengelolaan Aset Multimedia (Assets)

Direktori `assets/` ini digunakan untuk menyimpan seluruh berkas eksternal yang dibutuhkan dalam pembuatan animasi Manim video **Cara Kerja Transformers**.

## 📁 Struktur Direktori Aset

```text
assets/
├── audio/          # Tempat menyimpan file rekaman Voiceover (VO) & musik latar
│   ├── 01_hook.mp3
│   ├── 02_reframe.mp3
│   ├── 03_embedding.mp3
│   ├── 04_attention.mp3
│   ├── 05_layers.mp3
│   ├── 06_training.mp3
│   ├── 07_thinking.mp3
│   └── 08_outro.mp3
├── fonts/          # Tempat menyimpan custom font (misal: Inter-Regular.ttf, Roboto.ttf)
└── images/         # Tempat menyimpan gambar eksternal atau ikon SVG (logo, ikon otak, dll.)
```

---

## 🎙️ Tips Sinkronisasi Audio Voiceover (VO) di Manim

Untuk mensinkronisasikan rekaman suara narasi (Voiceover) dengan animasi geometris di Manim, Anda dapat memanfaatkan metode `self.add_sound()` di dalam metode `construct()` pada masing-masing scene.

### Contoh Kode Sinkronisasi Audio:
```python
class AttentionMechanismScene(Scene):
    def construct(self):
        # 1. Tambahkan audio voiceover untuk scene ini
        self.add_sound("assets/audio/04_attention.mp3")
        
        # 2. Atur durasi animasi agar pas dengan intonasi narator
        self.play(FadeIn(sentence), run_time=2.0)
        self.wait(1.5) # Jeda menunggu narator selesai menyebut kalimat penjelas
```

---

## 🎨 Penggunaan Custom SVG Icons

Jika Anda ingin menampilkan ikon vektor berkualitas tinggi (seperti ikon otak biologis atau logo OpenAI), simpan file berformat `.svg` ke dalam folder `assets/images/`, lalu panggil menggunakan kelas `SVGMobject` di Manim:

```python
from manim import *

class BrainIcon(SVGMobject):
    def __init__(self, **kwargs):
        super().__init__("assets/images/brain_icon.svg", **kwargs)
        self.set_color(RED_C)
```
