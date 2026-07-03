"""
[08:00 - 08:45] SCENE 8: PENUTUP (OUTRO & CALL TO ACTION)
Fokus Visual: Zoom out dari satu titik kata ke seluruh jaringan attention raksasa yang tadi ditampilkan,
lalu fade ke teks: "Bukan sihir. Statistik dalam skala luar biasa besar."
Call to action untuk Like, Subscribe, dan eksplorasi topik lanjutan (RLHF, Halusinasi).
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from manim import *
from src.constants import *

class OutroScene(Scene):
    def construct(self):
        self.camera.background_color = DARK_BG
        
        # 1. Animasi Zoom Out dari 1 Titik ke Jaringan Raksasa
        center_dot = Dot(point=ORIGIN, radius=0.3, color=YELLOW_3B1B)
        center_label = Text("Satu Kata / Token", font=FONT_PRIMARY, font_size=20, color=YELLOW_3B1B).next_to(center_dot, DOWN)
        
        self.play(FadeIn(center_dot), Write(center_label), run_time=1.0)
        self.wait(0.5)
        
        # Buat jaringan titik raksasa di sekelilingnya
        massive_net = VGroup()
        connections = VGroup()
        
        np.random.seed(42) # Agar hasil animasi konsisten
        for _ in range(60):
            pos = np.array([np.random.uniform(-6, 6), np.random.uniform(-3.5, 3.5), 0])
            col = np.random.choice([BLUE_3B1B, TEAL_3B1B, PURPLE_3B1B, GREEN_3B1B])
            dot = Dot(point=pos, radius=0.08, color=col)
            massive_net.add(dot)
            
            # Hubungan acak ke titik dekat
            if np.linalg.norm(pos) < 4.0 and np.random.random() > 0.6:
                line = Line(ORIGIN, pos, color=col, stroke_width=1, stroke_opacity=0.3)
                connections.add(line)
                
        self.play(
            FadeOut(center_label),
            center_dot.animate.scale(0.3),
            Create(connections),
            FadeIn(massive_net),
            run_time=2.5
        )
        self.wait(1.0)
        
        # 2. Fade ke Teks Kesimpulan Utama (Pesan Inti)
        self.play(
            massive_net.animate.set_opacity(0.15),
            connections.animate.set_opacity(0.1),
            run_time=1.0
        )
        
        quote_box = RoundedRectangle(corner_radius=0.3, width=11.0, height=2.0, fill_color=PANEL_BG, fill_opacity=0.9, stroke_color=YELLOW_3B1B, stroke_width=3)
        quote_box.move_to(UP * 0.8)
        
        quote_text = Text(
            "“Bukan Sihir.\nIni adalah Matematika & Statistik dalam Skala Luar Biasa Besar.”",
            font=FONT_MATH, font_size=32, color=YELLOW_3B1B, line_spacing=1.3
        ).move_to(quote_box.get_center())
        
        self.play(FadeIn(quote_box), Write(quote_text), run_time=2.0)
        self.wait(TIME_READING * 1.5)
        
        # 3. Call to Action (Like, Subscribe & Komentar topik selanjutnya)
        cta_box = VGroup()
        cta_text = Text("Penasaran gimana cara melatihnya biar sopan & tidak toxic (RLHF)?\nAtau kenapa dia bisa 'ngarang' fakta?", font=FONT_PRIMARY, font_size=22, color=WHITE_TEXT, line_spacing=1.2)
        cta_sub = Text("👉 Komen di bawah untuk video lanjutannya! | 👍 Like & Subscribe", font=FONT_PRIMARY, font_size=24, color=TEAL_3B1B)
        
        cta_box.add(cta_text, cta_sub).arrange(DOWN, buff=0.4)
        cta_box.move_to(DOWN * 2.0)
        
        self.play(FadeIn(cta_box, shift=UP * 0.3), run_time=1.5)
        self.wait(3.0)
        
        # Fade out akhir
        self.play(FadeOut(Group(*self.mobjects)), run_time=2.0)

if __name__ == "__main__":
    with tempconfig({"quality": "high_quality", "preview": True}):
        scene = OutroScene()
        scene.render()
