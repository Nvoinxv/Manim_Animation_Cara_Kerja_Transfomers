"""
[00:35 - 01:30] SCENE 2: REFRAME (INI BUKAN OTAK, INI MESIN PREDIKSI)
Fokus Visual: Animasi kalimat "Ibu kota Indonesia adalah ___" dengan blank di akhir,
lalu muncul beberapa kandidat kata melayang: "Jakarta" (besar, terang), "kucing" (kecil, redup),
"meja" (kecil, redup) — seolah mesin memilih probabilitas tertinggi.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from manim import *
from src.constants import *
from src.utils.layouts import create_probability_bar_chart
from src.utils.animations import animate_pulse

class NextWordPredictionScene(Scene):
    def construct(self):
        self.camera.background_color = DARK_BG
        
        # 1. Tampilkan judul konsep
        title = Text("Mesin Prediksi Statistik (Bukan Otak)", font=FONT_PRIMARY, font_size=FONT_SIZE_SUBTITLE, color=WHITE_TEXT)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=TIME_NORMAL)
        
        # 2. Kalimat prompt dengan blank "___"
        prompt_text = Text("Ibu kota Indonesia adalah ", font=FONT_PRIMARY, font_size=36, color=WHITE_TEXT)
        blank_box = RoundedRectangle(corner_radius=0.1, width=2.5, height=0.8, color=YELLOW_3B1B, stroke_width=3)
        question_mark = Text("?", font=FONT_PRIMARY, font_size=36, color=YELLOW_3B1B)
        question_mark.move_to(blank_box.get_center())
        
        sentence_group = VGroup(prompt_text, VGroup(blank_box, question_mark)).arrange(RIGHT, buff=0.2)
        sentence_group.move_to(UP * 1.5)
        
        self.play(FadeIn(prompt_text, shift=RIGHT * 0.5), Create(blank_box), Write(question_mark), run_time=TIME_NORMAL)
        self.wait(1.0)
        
        # 3. Kandidat kata melayang di bawah kalimat dengan probabilitas
        candidates = ["Jakarta", "Surabaya", "kucing", "meja", "matematika"]
        probs = [0.88, 0.08, 0.02, 0.01, 0.01]
        colors = [GREEN_3B1B, TEAL_3B1B, MUTED_TEXT, MUTED_TEXT, MUTED_TEXT]
        
        # Grafik batang probabilitas
        bar_chart = create_probability_bar_chart(candidates, probs, colors=colors, width=8.0)
        bar_chart.next_to(sentence_group, DOWN, buff=1.0)
        
        self.play(FadeIn(bar_chart, shift=UP * 0.5), run_time=1.5)
        self.wait(1.5)
        
        # 4. Sorot pemenang probabilitas tertinggi ("Jakarta")
        winner_row = bar_chart[0]
        self.play(animate_pulse(winner_row, scale_factor=1.1, color=YELLOW_3B1B))
        
        # 5. Animasi kata "Jakarta" terbang masuk ke dalam kotak blank
        winner_word = Text("Jakarta", font=FONT_PRIMARY, font_size=32, color=GREEN_3B1B)
        winner_word.move_to(winner_row[0].get_center())
        
        self.play(
            FadeOut(question_mark),
            winner_word.animate.move_to(blank_box.get_center()).scale(1.1),
            blank_box.animate.set_color(GREEN_3B1B).set_fill(color=GREEN_3B1B, opacity=0.2),
            run_time=TIME_SLOW
        )
        self.wait(TIME_READING)
        
        # 6. Kesimpulan: Tugas tunggal diulang terus-menerus
        loop_text = Text(
            "Dikasih teks sejauh ini -> Tebak kata paling mungkin -> Ulangi terus!",
            font=FONT_PRIMARY,
            font_size=24,
            color=BLUE_LIGHT
        ).to_edge(DOWN, buff=0.8)
        
        self.play(Write(loop_text), run_time=TIME_NORMAL)
        self.wait(TIME_READING)
        
        # Cleanup
        self.play(FadeOut(Group(*self.mobjects)), run_time=TIME_NORMAL)

if __name__ == "__main__":
    with tempconfig({"quality": "high_quality", "preview": True}):
        scene = NextWordPredictionScene()
        scene.render()
