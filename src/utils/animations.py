"""
Kumpulan animasi kustom (Custom Animations) untuk memperkaya visualisasi ala 3Blue1Brown.
Termasuk efek typewriter real-time, glowing highlight, dan denyut aksentuasi (pulse).
"""

from manim import *
from src.constants import *

def create_glowing_surround_rect(mobject, color=YELLOW_3B1B, buff=0.15, stroke_width=3, glow_factor=3):
    """
    Membuat kotak sorot (SurroundingRectangle) dengan efek bersinar (glow) berlapis.
    Sangat berguna untuk menyorot kata penting atau token yang sedang diproses.
    """
    core_rect = SurroundingRectangle(mobject, color=color, buff=buff, stroke_width=stroke_width, corner_radius=0.1)
    glow_rects = VGroup()
    
    for i in range(1, glow_factor + 1):
        glow = SurroundingRectangle(
            mobject,
            color=color,
            buff=buff + (0.05 * i),
            stroke_width=stroke_width / (i * 1.5),
            corner_radius=0.1 + (0.05 * i)
        )
        glow.set_opacity(0.4 / i)
        glow_rects.add(glow)
        
    return VGroup(glow_rects, core_rect)

class TypewriterText(Animation):
    """
    Animasi custom untuk memunculkan teks huruf demi huruf secara real-time
    seperti efek streaming ChatGPT atau typewriter.
    """
    def __init__(self, mobject: Text, run_time: float = 2.0, **kwargs):
        super().__init__(mobject, run_time=run_time, **kwargs)
        self.mobject.set_opacity(0)
        self.total_chars = len(self.mobject)

    def interpolate_mobject(self, alpha: float) -> None:
        # Menentukan jumlah karakter yang harus ditampilkan berdasarkan progres alpha
        chars_to_show = int(alpha * self.total_chars)
        for i, char in enumerate(self.mobject):
            if i <= chars_to_show:
                char.set_opacity(1)
            else:
                char.set_opacity(0)

def animate_pulse(mobject, scale_factor=1.15, color=HIGHLIGHT_GOLD, run_time=0.6):
    """
    Mengembalikan sequence animasi pulse (membesar sedikit lalu kembali normal)
    sambil berubah warna sementara untuk menarik perhatian penonton.
    """
    original_color = mobject.get_color()
    return Succession(
        mobject.animate.scale(scale_factor).set_color(color).set_run_time(run_time / 2),
        mobject.animate.scale(1 / scale_factor).set_color(original_color).set_run_time(run_time / 2)
    )

def create_floating_animation(mobject, amplitude=0.1, frequency=1.0):
    """
    Fungsi pengubah (updater) untuk membuat objek melayang halus naik-turun (floating/hovering).
    Sangat cocok untuk kata-kata kandidat probabilitas yang melayang di ruang vektor.
    """
    initial_y = mobject.get_y()
    def updater(mob, dt):
        # Menggunakan waktu internal scene jika memungkinkan atau akumulasi dt
        if not hasattr(mob, "time_elapsed"):
            mob.time_elapsed = 0
        mob.time_elapsed += dt
        new_y = initial_y + amplitude * np.sin(2 * np.pi * frequency * mob.time_elapsed)
        mob.set_y(new_y)
    return updater
