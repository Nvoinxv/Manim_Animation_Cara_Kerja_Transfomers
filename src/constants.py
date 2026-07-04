"""
Konstanta dan desain sistem untuk animasi Manim ala 3Blue1Brown.
Menyimpan palet warna, tipografi, ukuran standar, dan durasi animasi.
"""

from manim import *

# ==========================================
# 0. KONFIGURASI OTOMATIS RENDER (1080p 60FPS)
# ==========================================
# Memaksa Manim selalu merender 1080p 60fps meskipun dirun biasa (tanpa flag -pqh) di VS Code
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60

# ==========================================
# 1. PALET WARNA (3BLUE1BROWN STYLE & USER PREFERENCE)
# ==========================================
# Latar belakang hitam dicampur biru (Deep Navy / Midnight Blue ala permintaan user)
DARK_BG = "#0A1128"
PANEL_BG = "#162238"
PANEL_BORDER = "#3B82F6"

# Warna primer geometris ala Grant Sanderson
BLUE_3B1B = "#58C4DD"       # BLUE_D di Manim standar
BLUE_LIGHT = "#9DE0F6"
BLUE_DARK = "#1C758A"

YELLOW_3B1B = "#FFFF00"     # YELLOW_C
YELLOW_LIGHT = "#FFFFA1"
YELLOW_DARK = "#C7C700"

TEAL_3B1B = "#5CD0B3"       # TEAL_C
TEAL_LIGHT = "#99E5D1"
TEAL_DARK = "#29AB87"

GREEN_3B1B = "#83C167"      # GREEN_C
GREEN_LIGHT = "#A6CF8C"

PURPLE_3B1B = "#9A72AC"     # PURPLE_B
PURPLE_LIGHT = "#C19CD5"

RED_3B1B = "#FC6255"        # RED_C
RED_LIGHT = "#FF8080"

WHITE_TEXT = "#FFFFFF"
MUTED_TEXT = "#ADB5BD"
HIGHLIGHT_GOLD = "#FFD700"

# ==========================================
# 2. TIPOGRAFI & UKURAN FONT
# ==========================================
FONT_PRIMARY = "sans-serif"  # Bisa diganti "Inter" atau "Roboto" jika tersedia
FONT_CODE = "monospace"
FONT_MATH = "serif"

FONT_SIZE_TITLE = 48
FONT_SIZE_SUBTITLE = 36
FONT_SIZE_BODY = 28
FONT_SIZE_CAPTION = 20
FONT_SIZE_TOKEN = 24

# ==========================================
# 3. DURASI & KECEPATAN ANIMASI (TIMING)
# ==========================================
TIME_QUICK = 0.4        # Untuk micro-animation, highlight cepat
TIME_NORMAL = 0.8       # Untuk transisi standar (FadeIn, Transform)
TIME_SLOW = 1.5         # Untuk pergerakan kamera, rotasi 3D, atau penekanan
TIME_READING = 2.0      # Waktu jeda agar penonton bisa membaca teks

# ==========================================
# 4. DIMENSI & LAYOUT GRID
# ==========================================
FRAME_WIDTH = 14.222    # 16:9 aspect ratio width di Manim
FRAME_HEIGHT = 8.0      # 16:9 aspect ratio height di Manim

# Batas aman area gambar (Safe area margin)
MARGIN_X = 6.0
MARGIN_Y = 3.2
