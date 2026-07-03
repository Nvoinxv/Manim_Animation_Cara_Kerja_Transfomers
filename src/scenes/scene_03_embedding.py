"""
[01:30 - 02:45] SCENE 3: LANGKAH 1 - KATA DIUBAH JADI ANGKA (TOKEN & EMBEDDING)
Fokus Visual: Kata "kucing" pecah menjadi potongan token kecil, lalu tiap token berubah
menjadi titik di ruang 3D/2D (grafik vektor). Titik "kucing" muncul dekat titik "anjing",
jauh dari titik "mobil" atau "matematika" (Semantic Clustering).
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from manim import *
from src.constants import *
from src.components.word_embedder import TokenBox, WordEmbeddingSpace
from src.utils.layouts import create_vector_space_axes

class TokenAndEmbeddingScene(Scene):
    def construct(self):
        self.camera.background_color = DARK_BG
        
        # 1. Judul Langkah 1
        title = Text("Langkah 1: Token & Word Embedding Space", font=FONT_PRIMARY, font_size=FONT_SIZE_SUBTITLE, color=WHITE_TEXT)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=TIME_NORMAL)
        
        # 2. Kalimat dipecah menjadi Token (Tokenization)
        sample_sentence = ["Kucing", "itu", "tidur", "di", "atas", "kasur"]
        token_ids = [4123, 891, 10244, 45, 902, 31102]
        
        tokens_group = VGroup(*[
            TokenBox(word, tid, color=BLUE_3B1B if i == 0 else TEAL_3B1B)
            for i, (word, tid) in enumerate(zip(sample_sentence, token_ids))
        ]).arrange(RIGHT, buff=0.2)
        tokens_group.move_to(UP * 2.0)
        
        self.play(FadeIn(tokens_group, shift=DOWN * 0.3), run_time=1.0)
        self.wait(1.0)
        
        # Penjelasan Token
        token_caption = Text("Komputer tidak mengerti kata; teks dipotong menjadi unit angka (Token)", font=FONT_PRIMARY, font_size=22, color=MUTED_TEXT)
        token_caption.next_to(tokens_group, DOWN, buff=0.4)
        self.play(Write(token_caption), run_time=TIME_NORMAL)
        self.wait(1.5)
        
        # 3. Transisi ke Ruang Vektor (Embedding Space)
        self.play(
            FadeOut(token_caption),
            tokens_group[1:].animate.set_opacity(0.2),
            tokens_group[0].animate.scale(1.2).move_to(LEFT * 4 + UP * 0.5),
            run_time=TIME_NORMAL
        )
        
        # Buat ruang embedding 2D
        embed_space = WordEmbeddingSpace(width=8.5, height=5.0)
        embed_space.move_to(RIGHT * 2.2 + DOWN * 0.5)
        
        axes = create_vector_space_axes(dim=2, x_range=(-4, 4), y_range=(-2.5, 2.5))
        axes.move_to(embed_space.get_center())
        
        self.play(Create(embed_space), Create(axes), run_time=1.5)
        
        # 4. Petakan kata-kata ke ruang koordinat (Semantic Proximity)
        # Hewan berdekatan di kuadran kanan atas
        cat_node = embed_space.add_word_vector("kucing", RIGHT * 1.5 + UP * 1.2, color=YELLOW_3B1B)
        dog_node = embed_space.add_word_vector("anjing", RIGHT * 2.2 + UP * 1.5, color=YELLOW_3B1B)
        rabbit_node = embed_space.add_word_vector("kelinci", RIGHT * 1.8 + UP * 0.6, color=YELLOW_3B1B)
        
        # Kendaraan di kuadran kiri bawah
        car_node = embed_space.add_word_vector("mobil", LEFT * 2.0 + DOWN * 1.2, color=RED_3B1B)
        motor_node = embed_space.add_word_vector("motor", LEFT * 2.5 + DOWN * 0.8, color=RED_3B1B)
        
        # Konsep abstrak di kuadran kiri atas
        math_node = embed_space.add_word_vector("matematika", LEFT * 2.2 + UP * 1.5, color=PURPLE_3B1B)
        
        self.play(
            FadeIn(cat_node), FadeIn(dog_node), FadeIn(rabbit_node),
            FadeIn(car_node), FadeIn(motor_node), FadeIn(math_node),
            run_time=2.0
        )
        self.wait(1.0)
        
        # 5. Sorot Klaster Semantik & Jarak
        animal_cluster = embed_space.create_semantic_cluster_highlight(
            ["kucing", "anjing", "kelinci"], color=YELLOW_3B1B, label_text="Makna Dekat (Hewan)"
        )
        vehicle_cluster = embed_space.create_semantic_cluster_highlight(
            ["mobil", "motor"], color=RED_3B1B, label_text="Makna Dekat (Kendaraan)"
        )
        
        self.play(Create(animal_cluster), Create(vehicle_cluster), run_time=1.5)
        
        # Garis jarak semantik (kucing jauh dari mobil)
        dist_line = embed_space.create_distance_line("kucing", "mobil", color=WHITE_TEXT)
        self.play(Create(dist_line), run_time=TIME_NORMAL)
        self.wait(TIME_READING)
        
        # 6. Kesimpulan Langkah 1
        summary = Text(
            "Kata berubah menjadi koordinat angka berdimensi tinggi yang menyimpan JEJAK MAKNA.",
            font=FONT_PRIMARY, font_size=22, color=BLUE_LIGHT
        ).to_edge(DOWN, buff=0.4)
        
        self.play(Write(summary), run_time=TIME_NORMAL)
        self.wait(TIME_READING)
        
        # Cleanup
        self.play(FadeOut(Group(*self.mobjects)), run_time=TIME_NORMAL)
