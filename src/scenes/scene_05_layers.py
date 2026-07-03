"""
[05:00 - 06:15] SCENE 5: LANGKAH 3 - SEMUA INFO DIOLAH BERLAPIS-LAPIS
Fokus Visual: Tumpukan kotak transparan (layer) dari bawah ke atas, tiap layer sedikit
mengubah warna/posisi titik kata, sampai di layer paling atas titiknya sudah jauh berbeda
dari awal (Hierarchical Abstraction / Deep Learning Layers).
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from manim import *
from src.constants import *
from src.components.layer_stack import LayerStack

class LayerProcessingScene(Scene):
    def construct(self):
        self.camera.background_color = DARK_BG
        
        # 1. Judul Langkah 3
        title = Text("Langkah 3: Diproses Berlapis-lapis (Deep Transformer Layers)", font=FONT_PRIMARY, font_size=FONT_SIZE_SUBTITLE, color=WHITE_TEXT)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=TIME_NORMAL)
        
        # 2. Munculkan Tumpukan Layer (Layer Stack)
        stack = LayerStack(num_layers=4, layer_width=9.0, layer_height=1.0, spacing=1.4)
        stack.move_to(DOWN * 0.5)
        
        self.play(FadeIn(stack, shift=UP * 0.5), run_time=1.5)
        self.wait(1.0)
        
        # 3. Animasi Aliran Data/Token melewati lapisan demi lapisan
        token_dot = Dot(radius=0.25, color=BLUE_3B1B)
        token_label = Text("Token: 'dia'", font=FONT_PRIMARY, font_size=20, color=WHITE_TEXT)
        token_label.add_updater(lambda m: m.next_to(token_dot, RIGHT, buff=0.2))
        
        self.play(FadeIn(token_dot), FadeIn(token_label), run_time=0.5)
        
        # Jalankan animasi data flow naik ke atas
        data_flow = stack.animate_data_flow(token_dot, start_color=BLUE_3B1B, end_color=PURPLE_3B1B, run_time=4.0)
        self.play(data_flow)
        self.wait(1.0)
        
        # 4. Penjelasan Transformasi Makna per Layer
        token_label.clear_updaters()
        self.play(
            token_label.animate.become(
                Text("Pemahaman Abstrak: 'dia' = Kucing yang sedang kelelahan", font=FONT_PRIMARY, font_size=22, color=YELLOW_3B1B)
                .next_to(stack.layers[-1], UP, buff=0.4)
            )
        )
        self.wait(1.5)
        
        # 5. Kesimpulan Langkah 3: Siap menebak kata berikutnya
        summary_box = RoundedRectangle(corner_radius=0.15, width=11.0, height=1.2, fill_color=PANEL_BG, fill_opacity=0.9, stroke_color=TEAL_3B1B, stroke_width=2)
        summary_box.to_edge(DOWN, buff=0.4)
        
        summary_text = Text(
            "Setelah melewati puluhan lapisan pemahaman abstrak ini...\n"
            "Barulah model punya cukup 'konteks' untuk akurat MENEBAK KATA BERIKUTNYA!",
            font=FONT_PRIMARY, font_size=22, color=WHITE_TEXT, line_spacing=1.2
        ).move_to(summary_box.get_center())
        
        self.play(FadeIn(summary_box), Write(summary_text), run_time=2.0)
        self.wait(TIME_READING * 1.5)
        
        # Cleanup
        self.play(FadeOut(Group(*self.mobjects)), run_time=TIME_NORMAL)

if __name__ == "__main__":
    with tempconfig({"quality": "high_quality", "preview": True}):
        scene = LayerProcessingScene()
        scene.render()
