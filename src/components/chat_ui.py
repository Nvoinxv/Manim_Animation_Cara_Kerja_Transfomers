"""
Komponen antarmuka (UI) ChatGPT Mockup.
Menampilkan jendela chat bergaya modern dengan gelembung pertanyaan user
dan jawaban streaming kata demi kata (real-time word prediction).
Perbaikan: Posisi tombol dots diperbaiki ke kiri header, teks full putih (#FFFFFF).
"""

from manim import *
from src.constants import *

class ChatGPTUI(VGroup):
    def __init__(self, width=11.0, height=6.5, **kwargs):
        super().__init__(**kwargs)
        self.width = width
        self.height = height
        
        # 1. Background Window Frame (Lebih terang dari latar belakang agar kontras dan jelas)
        self.window = RoundedRectangle(
            corner_radius=0.3,
            width=self.width,
            height=self.height,
            fill_color=PANEL_BG,
            fill_opacity=0.95,
            stroke_color=PANEL_BORDER,
            stroke_width=2.5
        )
        
        # 2. Header Bar
        self.header = RoundedRectangle(
            corner_radius=0.3,
            width=self.width,
            height=0.8,
            fill_color="#0F172A",  # Dark slate navy
            fill_opacity=1.0,
            stroke_width=0
        )
        self.header.align_to(self.window, UP)
        
        # Judul Header (Full Putih)
        self.title_text = Text("ChatGPT (Model: GPT-4o / Transformer)", font=FONT_PRIMARY, font_size=20, color="#FFFFFF")
        self.title_text.move_to(self.header.get_center())
        
        # Tombol window (macOS style dots) - PERBAIKAN POSISI: move_to ke sisi kiri header!
        self.dots = VGroup(*[
            Circle(radius=0.08, fill_color=col, fill_opacity=1, stroke_width=0)
            for col in [RED_3B1B, YELLOW_3B1B, GREEN_3B1B]
        ]).arrange(RIGHT, buff=0.15)
        self.dots.move_to(self.header.get_left() + RIGHT * 0.6)
        
        # Garis pemisah header
        self.divider = Line(
            self.header.get_bottom() + LEFT * (self.width / 2),
            self.header.get_bottom() + RIGHT * (self.width / 2),
            color=PANEL_BORDER,
            stroke_width=1.5
        )
        
        self.add(self.window, self.header, self.title_text, self.dots, self.divider)
        self.content_area_top = self.header.get_bottom() + DOWN * 0.4
        
    def create_user_prompt(self, prompt_text="Apa itu ChatGPT dan bagaimana cara kerjanya?", return_parts=False):
        text = Text(prompt_text, font=FONT_PRIMARY, font_size=22, color=WHITE_TEXT)
        text.set_max_width(self.width * 0.7)
 
        bubble = RoundedRectangle(
            corner_radius=0.2,
            width=text.width + 0.6,
            height=text.height + 0.4,
            fill_color=BLUE_DARK,
            fill_opacity=0.8,
            stroke_color=BLUE_3B1B,
            stroke_width=1
        )
 
        group = VGroup(bubble, text)
        text.move_to(bubble.get_center())
 
        group.move_to(self.content_area_top + DOWN * (bubble.height / 2))
        group.align_to(self.window, RIGHT).shift(LEFT * 0.5)
 
        if return_parts:
            # group  -> dipakai kalau cuma butuh FadeIn/FadeOut sekaligus
            # bubble -> dipakai buat FadeIn duluan sebelum teks muncul
            # text   -> dipakai buat animasi Write() + cursor mengikuti posisinya
            return group, bubble, text
        return group
        
    def create_ai_response_words(self, response_text="ChatGPT tidak tahu jawaban dari awal. Dia hanya nebak satu kata berikutnya."):
        """
        Memecah teks balasan AI menjadi daftar mobjects kata individual (Full Putih #FFFFFF)
        agar bisa dianimasikan muncul satu per satu (word-by-word prediction).
        """
        words = response_text.split()
        word_mobjects = VGroup()
        
        for word in words:
            word_mob = Text(word, font=FONT_PRIMARY, font_size=24, color="#FFFFFF")
            word_mobjects.add(word_mob)
            
        # Atur layout kata secara otomatis (wrapping di dalam window)
        max_width = self.width * 0.85
        current_line = VGroup()
        lines = VGroup()
        
        for w in word_mobjects:
            current_line.add(w)
            current_line.arrange(RIGHT, buff=0.15)
            if current_line.width > max_width:
                current_line.remove(w)
                lines.add(current_line)
                current_line = VGroup(w)
                
        if len(current_line) > 0:
            lines.add(current_line)
            
        lines.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        lines.align_to(self.window, LEFT).shift(RIGHT * 0.6)
        
        # Posisikan di bawah gelembung user
        lines.set_y(self.content_area_top[1] - 2.0)
        
        return word_mobjects
