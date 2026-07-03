"""
[06:15 - 07:00] SCENE 6: KENAPA DIA BISA SEPINTER INI? (SEKILAS TRAINING)
Fokus Visual: Animasi jutaan halaman teks (buku, artikel, website) "disedot" masuk
ke dalam kotak model, lalu keluar sebagai jaringan titik-titik yang makin rapi/terorganisir.
Menjelaskan proses belajar iteratif (tebak -> cek error -> koreksi sedikit -> ulang triliunan kali).
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from manim import *
from src.constants import *
from src.utils.animations import animate_pulse

class TrainingOverviewScene(Scene):
    def construct(self):
        self.camera.background_color = DARK_BG
        
        # 1. Judul Training
        title = Text("Sekilas Training: Belajar dari Data dalam Skala Raksasa", font=FONT_PRIMARY, font_size=FONT_SIZE_SUBTITLE, color=WHITE_TEXT)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=TIME_NORMAL)
        
        # 2. Kotak Model Transformer di Tengah
        model_box = RoundedRectangle(corner_radius=0.3, width=3.5, height=3.5, fill_color=PANEL_BG, fill_opacity=0.9, stroke_color=BLUE_3B1B, stroke_width=3)
        model_label = Text("Transformer\nModel", font=FONT_PRIMARY, font_size=24, color=BLUE_3B1B).move_to(model_box.get_center())
        model_group = VGroup(model_box, model_label).move_to(ORIGIN)
        
        self.play(FadeIn(model_group), run_time=1.0)
        
        # 3. Animasi Data Masif (Buku, Artikel, Web) "disedot" masuk dari kiri
        data_sources = VGroup()
        for i in range(8):
            doc = RoundedRectangle(corner_radius=0.05, width=0.8, height=1.1, fill_color=TEAL_3B1B, fill_opacity=0.6, stroke_width=1)
            # Garis-garis teks di dalam dokumen
            lines = VGroup(*[Line(LEFT*0.25, RIGHT*0.25, stroke_width=2, color=DARK_BG) for _ in range(3)]).arrange(DOWN, buff=0.15)
            lines.move_to(doc.get_center())
            doc_group = VGroup(doc, lines)
            
            # Posisi acak di sebelah kiri
            start_pos = LEFT * 6.0 + UP * np.random.uniform(-2.5, 2.5) + RIGHT * np.random.uniform(0, 1.5)
            doc_group.move_to(start_pos)
            data_sources.add(doc_group)
            
        self.play(FadeIn(data_sources), run_time=1.0)
        
        # Animasi menyedot data ke dalam kotak model
        absorb_anims = []
        for doc in data_sources:
            absorb_anims.append(
                doc.animate.move_to(model_box.get_center()).scale(0.1).set_opacity(0)
            )
            
        self.play(*absorb_anims, animate_pulse(model_box, scale_factor=1.2, color=YELLOW_3B1B), run_time=2.5)
        self.wait(0.5)
        
        # 4. Keluaran di sebelah kanan: Jaringan Titik-titik (Knowledge Network) yang makin terstruktur
        network_dots = VGroup()
        connections = VGroup()
        
        # Titik-titik dalam formasi melingkar / teratur
        angles = np.linspace(0, 2 * np.pi, 10, endpoint=False)
        for idx, ang in enumerate(angles):
            pos = RIGHT * 4.5 + np.array([1.8 * np.cos(ang), 1.8 * np.sin(ang), 0])
            dot = Dot(point=pos, radius=0.12, color=YELLOW_3B1B if idx % 2 == 0 else PURPLE_3B1B)
            network_dots.add(dot)
            
        # Hubungan antar titik
        for i in range(len(network_dots)):
            for j in range(i + 1, len(network_dots)):
                if np.random.random() > 0.5:
                    line = Line(network_dots[i].get_center(), network_dots[j].get_center(), color=MUTED_TEXT, stroke_width=1, stroke_opacity=0.4)
                    connections.add(line)
                    
        network_group = VGroup(connections, network_dots)
        
        # Animasi panah keluar dari model ke jaringan
        out_arrow = Arrow(model_box.get_right(), RIGHT * 2.5, color=YELLOW_3B1B, stroke_width=4)
        self.play(Create(out_arrow), run_time=0.5)
        self.play(Create(connections), FadeIn(network_dots, scale=0.5), run_time=2.0)
        self.wait(1.0)
        
        # 5. Penjelasan Proses Iteratif (Tebak -> Koreksi -> Ulang)
        iter_box = RoundedRectangle(corner_radius=0.15, width=12.0, height=1.3, fill_color=PANEL_BG, fill_opacity=0.9, stroke_color=GREEN_3B1B, stroke_width=2)
        iter_box.to_edge(DOWN, buff=0.4)
        
        iter_text = Text(
            "Cara Belajar: Tebak kata berikutnya -> Cek jawaban -> Koreksi sedikit error-nya.\n"
            "Diulang TRILIUNAN KALI sampai pola bahasa, fakta, dan logika terbentuk sendiri!",
            font=FONT_PRIMARY, font_size=22, color=WHITE_TEXT, line_spacing=1.2
        ).move_to(iter_box.get_center())
        
        self.play(FadeIn(iter_box), Write(iter_text), run_time=2.0)
        self.wait(TIME_READING * 1.5)
        
        # Cleanup
        self.play(FadeOut(Group(*self.mobjects)), run_time=TIME_NORMAL)

if __name__ == "__main__":
    with tempconfig({"quality": "high_quality", "preview": True}):
        scene = TrainingOverviewScene()
        scene.render()
