"""
[07:00 - 08:00] SCENE 7: JADI, APAKAH DIA BENERAN "MIKIR"?
Fokus Visual: Split screen — kiri gambar otak manusia dengan koneksi neuron biologis,
kanan jaringan titik-titik angka (statistik matematis).
Lalu keduanya perlahan pudar menjadi tanda tanya besar dan penjelasan konsep Halusinasi.
"""

from manim import *
from src.constants import *

class ThinkingVsStatScene(Scene):
    def construct(self):
        self.camera.background_color = DARK_BG
        
        # 1. Judul Pertanyaan Filosofis
        title = Text("Apakah ChatGPT Beneran 'Mikir'?", font=FONT_PRIMARY, font_size=FONT_SIZE_SUBTITLE, color=WHITE_TEXT)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=TIME_NORMAL)
        
        # 2. Split Screen: Kiri (Otak Biologis) vs Kanan (Statistik Matematika)
        divider = Line(UP * 2.5, DOWN * 2.5, color=PANEL_BORDER, stroke_width=2)
        self.play(Create(divider), run_time=0.5)
        
        # KIRI: Otak Biologis
        left_title = Text("Otak Manusia", font=FONT_PRIMARY, font_size=26, color=RED_3B1B).move_to(LEFT * 3.5 + UP * 2.2)
        left_desc = Text("• Punya kesadaran & emosi\n• Pengalaman dunia nyata\n• Memahami makna sejati", font=FONT_PRIMARY, font_size=20, color=WHITE_TEXT, line_spacing=1.3).next_to(left_title, DOWN, buff=0.5)
        
        # KANAN: Mesin Statistik
        right_title = Text("Mesin Transformer", font=FONT_PRIMARY, font_size=26, color=BLUE_3B1B).move_to(RIGHT * 3.5 + UP * 2.2)
        right_desc = Text("• Tidak punya kesadaran\n• Hanya koordinat angka\n• Pola statistik super canggih", font=FONT_PRIMARY, font_size=20, color=WHITE_TEXT, line_spacing=1.3).next_to(right_title, DOWN, buff=0.5)
        
        self.play(
            FadeIn(left_title), FadeIn(left_desc),
            FadeIn(right_title), FadeIn(right_desc),
            run_time=1.5
        )
        self.wait(TIME_READING * 1.5)
        
        # 3. Pudar menjadi Tanda Tanya Besar
        split_group = VGroup(divider, left_title, left_desc, right_title, right_desc)
        big_question = Text("?", font=FONT_MATH, font_size=140, color=YELLOW_3B1B).move_to(ORIGIN)
        
        self.play(
            ReplacementTransform(split_group, big_question),
            run_time=1.5
        )
        self.wait(1.0)
        
        # 4. Penjelasan Halusinasi (Kenapa bisa keliru dengan percaya diri)
        self.play(big_question.animate.scale(0.4).move_to(UP * 1.2), run_time=0.8)
        
        halusinasi_box = RoundedRectangle(corner_radius=0.2, width=12.0, height=2.2, fill_color=PANEL_BG, fill_opacity=0.95, stroke_color=RED_3B1B, stroke_width=2)
        halusinasi_box.move_to(DOWN * 1.2)
        
        halusinasi_title = Text("Kenapa Bisa 'Halusinasi' (Keliru dengan Pede)?", font=FONT_PRIMARY, font_size=24, color=RED_3B1B)
        halusinasi_title.next_to(halusinasi_box.get_top(), DOWN, buff=0.2)
        
        halusinasi_desc = Text(
            "Karena tujuan utama mesin BUKAN 'berkata jujur atau mencari kebenaran absolut'.\n"
            "Tujuannya hanyalah: 'Menghasilkan kata yang secara statistik paling mungkin muncul selanjutnya'.\n"
            "Jika polanya keliru, dia akan tetap menjawab dengan susunan kata yang sangat meyakinkan!",
            font=FONT_PRIMARY, font_size=20, color=WHITE_TEXT, line_spacing=1.2
        ).next_to(halusinasi_title, DOWN, buff=0.2)
        
        self.play(FadeIn(halusinasi_box), Write(halusinasi_title), FadeIn(halusinasi_desc), run_time=2.0)
        self.wait(TIME_READING * 2.0)
        
        # Cleanup
        self.play(FadeOut(Group(*self.mobjects)), run_time=TIME_NORMAL)
