"""
[02:45 - 05:00] SCENE 4: LANGKAH 2 - ATTENTION MECHANISM (KLIMAKS VIDEO)
Fokus Visual: INI BAGIAN PALING PENTING DAN DURASI TERLAMA.
Tampilkan kalimat: "Kucing itu tidur di atas kasur karena **dia** capek."
Highlight kata "dia" lalu tarik garis panah dengan ketebalan berbeda ke tiap kata sebelumnya:
garis paling tebal ke "kucing", garis tipis ke "kasur", "tidur", dll (Heatmap koneksi).
Visualisasikan juga Multi-Head Attention (ratusan lampu sorot jalan bersamaan).
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from manim import *
from src.constants import *
from src.components.attention_net import AttentionSentence
from src.utils.animations import animate_pulse

class AttentionMechanismScene(Scene):
    def construct(self):
        self.camera.background_color = DARK_BG
        
        # 1. Judul Klimaks
        title = Text("Langkah 2: Attention Mechanism (Inti dari Semuanya)", font=FONT_PRIMARY, font_size=FONT_SIZE_SUBTITLE, color=WHITE_TEXT)
        title.to_edge(UP, buff=0.4)
        subtitle = Text("“Attention is All You Need” — Menghubungkan Konteks Antarkata", font=FONT_PRIMARY, font_size=20, color=YELLOW_3B1B)
        subtitle.next_to(title, DOWN, buff=0.1)
        
        self.play(Write(title), FadeIn(subtitle), run_time=1.0)
        
        # 2. Kalimat Analogi Utama
        words_list = ["Kucing", "itu", "tidur", "di", "atas", "kasur", "karena", "dia", "capek."]
        sentence = AttentionSentence(words_list)
        sentence.move_to(UP * 0.5)
        
        self.play(FadeIn(sentence, shift=DOWN * 0.5), run_time=1.5)
        self.wait(1.0)
        
        # 3. Sorot Pertanyaan Kunci: "Kata 'dia' merujuk ke siapa?"
        highlight_anim, glow_box = sentence.highlight_query_word("dia", color=YELLOW_3B1B)
        self.play(highlight_anim, Create(glow_box), run_time=TIME_NORMAL)
        
        question_text = Text("Kata 'dia' di sini merujuk ke siapa? Kucing atau Kasur?", font=FONT_PRIMARY, font_size=26, color=YELLOW_3B1B)
        question_text.next_to(sentence, DOWN, buff=1.0)
        self.play(Write(question_text), run_time=TIME_NORMAL)
        self.wait(1.5)
        
        # 4. Animasi Attention Weights (Heatmap Arrows)
        # Skor bobot: Kucing (0.85 - sangat tinggi), Kasur (0.10 - rendah), Tidur (0.05 - sangat rendah)
        weights = {
            "Kucing": 0.85,
            "kasur": 0.10,
            "tidur": 0.05
        }
        
        self.play(FadeOut(question_text), run_time=0.5)
        
        attention_arrows = sentence.create_attention_arrows("dia", weights)
        self.play(Create(attention_arrows), run_time=2.5)
        self.wait(1.5)
        
        # Penjelasan Bobot Attention
        exp_box = RoundedRectangle(corner_radius=0.2, width=12.0, height=1.8, fill_color=PANEL_BG, fill_opacity=0.9, stroke_color=YELLOW_3B1B, stroke_width=2)
        exp_box.to_edge(DOWN, buff=0.5)
        
        exp_text = Text(
            "Mesin memberi SKOR RELEVANSI tinggi (85%) ke kata 'Kucing'!\n"
            "Secara makna dan struktur kalimat, 'kucing' paling logis menjelaskan siapa 'dia'.\n"
            "Inilah yang membuat ChatGPT paham konteks, bukan sekadar membaca kata terpisah.",
            font=FONT_PRIMARY, font_size=22, color=WHITE_TEXT, line_spacing=1.2
        ).move_to(exp_box.get_center())
        
        self.play(FadeIn(exp_box), Write(exp_text), run_time=2.0)
        self.wait(TIME_READING * 1.5)
        
        # 5. Transisi ke Multi-Head Attention (Ratusan Lampu Sorot)
        self.play(
            FadeOut(attention_arrows),
            FadeOut(exp_box),
            FadeOut(exp_text),
            run_time=TIME_NORMAL
        )
        
        mha_title = Text("Multi-Head Attention: Ratusan 'Lampu Sorot' Berjalan Bersamaan", font=FONT_PRIMARY, font_size=26, color=TEAL_3B1B)
        mha_title.next_to(sentence, DOWN, buff=0.8)
        self.play(Write(mha_title), run_time=TIME_NORMAL)
        
        # Buat lampu sorot warna-warni ke berbagai aspek
        beams = sentence.create_spotlight_beams("dia", ["Kucing", "tidur", "capek."], colors=[YELLOW_3B1B, TEAL_3B1B, PURPLE_3B1B])
        self.play(FadeIn(beams), run_time=1.5)
        
        # Keterangan Head
        head1 = Text("Head 1: Fokus Makna Subjek (Kucing)", font=FONT_PRIMARY, font_size=18, color=YELLOW_3B1B).next_to(mha_title, DOWN, buff=0.3).to_edge(LEFT, buff=1.5)
        head2 = Text("Head 2: Fokus Tata Bahasa / Kata Kerja (tidur)", font=FONT_PRIMARY, font_size=18, color=TEAL_3B1B).next_to(mha_title, DOWN, buff=0.3)
        head3 = Text("Head 3: Fokus Kondisi/Sebab (capek)", font=FONT_PRIMARY, font_size=18, color=PURPLE_3B1B).next_to(mha_title, DOWN, buff=0.3).to_edge(RIGHT, buff=1.5)
        
        self.play(FadeIn(head1), FadeIn(head2), FadeIn(head3), run_time=1.5)
        self.wait(TIME_READING * 1.5)
        
        # Cleanup
        self.play(FadeOut(Group(*self.mobjects)), run_time=TIME_NORMAL)
