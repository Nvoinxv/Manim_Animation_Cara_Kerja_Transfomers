"""
Komponen visual untuk Mekanisme Attention (Attention Mechanism) - KLIMAKS VIDEO.
Menampilkan hubungan antarkata (seperti "dia" merujuk ke "kucing") menggunakan
panah bergaya heatmap dengan ketebalan dan opasitas proporsional terhadap bobot attention,
serta efek lampu sorot (spotlight) multi-head attention.
"""

from manim import *
from src.constants import *

class AttentionSentence(VGroup):
    """
    Menampilkan satu kalimat horizontal dengan kemampuan menyorot bobot koneksi attention
    antar kata menggunakan anak panah melengkung (CurvedArrow) ala heatmap.
    """
    def __init__(self, words: list[str], spacing=1.2, **kwargs):
        super().__init__(**kwargs)
        self.words = words
        self.word_mobs = VGroup()
        self.boxes = VGroup()
        
        for w in words:
            txt = Text(w, font=FONT_PRIMARY, font_size=32, color=WHITE_TEXT)
            box = RoundedRectangle(
                corner_radius=0.1,
                width=max(txt.width + 0.4, 1.0),
                height=txt.height + 0.4,
                fill_color=PANEL_BG,
                fill_opacity=0.8,
                stroke_color=PANEL_BORDER,
                stroke_width=1.5
            )
            txt.move_to(box.get_center())
            group = VGroup(box, txt)
            self.word_mobs.add(txt)
            self.boxes.add(box)
            self.add(group)
            
        self.arrange(RIGHT, buff=0.35)
        self.move_to(ORIGIN)
        
    def get_word_index(self, word_str: str):
        for i, w in enumerate(self.words):
            if w.lower().strip(".") == word_str.lower().strip("."):
                return i
        return -1
        
    def highlight_query_word(self, word_str: str, color=YELLOW_3B1B):
        """
        Menyorot kata utama (Query) yang sedang mencari konteks (misal: "dia").
        """
        idx = self.get_word_index(word_str)
        if idx == -1: return VGroup()
        
        target_box = self.boxes[idx]
        target_text = self.word_mobs[idx]
        
        glow = SurroundingRectangle(target_box, color=color, buff=0.1, stroke_width=4, corner_radius=0.15)
        
        return Succession(
            target_box.animate.set_stroke(color=color, width=3).set_fill(color=color, opacity=0.3),
            target_text.animate.set_color(color)
        ), glow
        
    def create_attention_arrows(self, query_word: str, target_weights: dict[str, float], base_color=BLUE_3B1B):
        """
        Membuat kumpulan panah melengkung dari kata query ke kata-kata lain.
        Ketebalan (stroke_width) dan opasitas diatur secara matematis oleh bobot probabilitas (0.0 - 1.0).
        
        Example target_weights:
            {"kucing": 0.85, "kasur": 0.10, "tidur": 0.05}
        """
        q_idx = self.get_word_index(query_word)
        if q_idx == -1: return VGroup()
        
        q_box = self.boxes[q_idx]
        arrows_group = VGroup()
        labels_group = VGroup()
        
        for t_word, weight in target_weights.items():
            t_idx = self.get_word_index(t_word)
            if t_idx == -1 or t_idx == q_idx: continue
            
            t_box = self.boxes[t_idx]
            
            # Hitung ketebalan dan warna berdasarkan bobot (Heatmap style)
            # Bobot tinggi -> Garis tebal, warna terang (Yellow/Teal)
            # Bobot rendah -> Garis tipis, warna redup (Blue/Muted)
            if weight > 0.6:
                arr_color = YELLOW_3B1B
                stroke_w = 8.0 * weight
                opacity = 1.0
            elif weight > 0.2:
                arr_color = TEAL_3B1B
                stroke_w = 4.0 * weight
                opacity = 0.8
            else:
                arr_color = base_color
                stroke_w = 2.0 * max(weight, 0.2)
                opacity = 0.4
                
            # Panah melengkung di atas kalimat
            angle = -0.6 if t_idx < q_idx else 0.6
            arrow = CurvedArrow(
                q_box.get_top() + UP * 0.1,
                t_box.get_top() + UP * 0.1,
                angle=angle,
                color=arr_color,
                stroke_width=stroke_w
            )
            arrow.set_opacity(opacity)
            
            # Label skor persentase attention (misal: 85%)
            score_text = Text(f"{int(weight * 100)}%", font=FONT_CODE, font_size=16, color=arr_color)
            score_text.set_opacity(opacity)
            score_text.next_to(arrow.get_center(), UP, buff=0.1)
            
            arrows_group.add(arrow)
            labels_group.add(score_text)
            
        return VGroup(arrows_group, labels_group)
        
    def create_spotlight_beams(self, query_word: str, target_words: list[str], colors=[YELLOW_3B1B, TEAL_3B1B, PURPLE_3B1B]):
        """
        Representasi visual Multi-Head Attention berupa lampu sorot (spotlight beams)
        berwarna-warni yang memancar dari kata query ke berbagai aspek makna/tata bahasa.
        """
        q_idx = self.get_word_index(query_word)
        if q_idx == -1: return VGroup()
        
        q_point = self.boxes[q_idx].get_bottom() + DOWN * 0.2
        beams = VGroup()
        
        for i, t_word in enumerate(target_words):
            t_idx = self.get_word_index(t_word)
            if t_idx == -1: continue
            
            t_box = self.boxes[t_idx]
            col = colors[i % len(colors)]
            
            # Segitiga transparan melambangkan sorotan cahaya
            beam = Polygon(
                q_point,
                t_box.get_bottom() + LEFT * (t_box.width / 2),
                t_box.get_bottom() + RIGHT * (t_box.width / 2),
                fill_color=col,
                fill_opacity=0.25,
                stroke_color=col,
                stroke_width=1.5,
                stroke_opacity=0.6
            )
            beams.add(beam)
            
        return beams
