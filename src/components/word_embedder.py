"""
Komponen visual untuk Tokenization dan Word Embedding Space (Ruang Vektor 2D/3D).
Menampilkan bagaimana kata dipecah menjadi token angka dan dipetakan ke koordinat
di mana kata dengan makna mirip berdekatan ("kucing" dekat "anjing", jauh dari "mobil").
"""

from manim import *
from src.constants import *

class TokenBox(VGroup):
    """
    Representasi visual satu token kata berupa kotak bergaya dengan angka ID token di bawahnya.
    """
    def __init__(self, word: str, token_id: int, color=BLUE_3B1B, **kwargs):
        super().__init__(**kwargs)
        self.word = word
        self.token_id = token_id
        
        # Teks Kata
        self.word_text = Text(word, font=FONT_PRIMARY, font_size=FONT_SIZE_TOKEN, color=WHITE_TEXT)
        
        # Kotak Token
        self.box = RoundedRectangle(
            corner_radius=0.15,
            width=max(self.word_text.width + 0.5, 1.2),
            height=self.word_text.height + 0.4,
            fill_color=color,
            fill_opacity=0.2,
            stroke_color=color,
            stroke_width=2
        )
        self.word_text.move_to(self.box.get_center())
        
        # Angka ID Token (Embedding Index)
        self.id_text = Text(f"#{token_id}", font=FONT_CODE, font_size=16, color=YELLOW_3B1B)
        self.id_text.next_to(self.box, DOWN, buff=0.15)
        
        self.add(self.box, self.word_text, self.id_text)

class WordEmbeddingSpace(VGroup):
    """
    Ruang vektor 2D untuk memvisualisasikan hubungan semantik antarkata
    berdasarkan jarak Euclidean/Cosine similarity.
    """
    def __init__(self, width=10, height=6, **kwargs):
        super().__init__(**kwargs)
        self.width = width
        self.height = height
        
        # Frame batas ruang vektor
        self.frame = Rectangle(width=width, height=height, stroke_color=PANEL_BORDER, stroke_width=1, stroke_opacity=0.5)
        
        # Grid latar belakang
        self.grid = NumberPlane(
            x_range=(-width/2, width/2, 1),
            y_range=(-height/2, height/2, 1),
            background_line_style={
                "stroke_color": PANEL_BORDER,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            }
        )
        self.grid.move_to(ORIGIN)
        self.add(self.grid)
        self.dots_map = {}
        self.labels_map = {}
        
    def add_word_vector(self, word: str, coords: np.ndarray, color=TEAL_3B1B, dot_size=0.12):
        """
        Menambahkan titik koordinat kata ke dalam ruang embedding.
        """
        dot = Dot(point=coords, radius=dot_size, color=color)
        dot.set_glow_factor(2)
        
        label = Text(word, font=FONT_PRIMARY, font_size=20, color=WHITE_TEXT)
        label.next_to(dot, UP, buff=0.15)
        
        group = VGroup(dot, label)
        self.dots_map[word] = dot
        self.labels_map[word] = label
        self.add(group)
        return group
        
    def create_semantic_cluster_highlight(self, words: list[str], color=YELLOW_3B1B, label_text="Cluster Makna Hewan"):
        """
        Membuat lingkaran sorot melingkari kelompok kata yang maknanya dekat.
        """
        dots = [self.dots_map[w] for w in words if w in self.dots_map]
        if not dots:
            return VGroup()
            
        cluster_group = VGroup(*dots)
        surround_circle = Circle(color=color, stroke_width=2, stroke_opacity=0.8)
        surround_circle.surround(cluster_group, buff=0.6)
        
        # Background transparan untuk cluster
        surround_circle.set_fill(color=color, opacity=0.1)
        
        title = Text(label_text, font=FONT_PRIMARY, font_size=18, color=color)
        title.next_to(surround_circle, UP, buff=0.1)
        
        return VGroup(surround_circle, title)
        
    def create_distance_line(self, word1: str, word2: str, color=RED_3B1B, show_distance=True):
        """
        Menarik garis putus-putus antara dua kata untuk menunjukkan jarak semantik (jauh/dekat).
        """
        p1 = self.dots_map[word1].get_center()
        p2 = self.dots_map[word2].get_center()
        
        line = DashedLine(p1, p2, dash_length=0.1, color=color, stroke_width=2)
        
        if show_distance:
            dist_val = np.linalg.norm(p1 - p2)
            dist_label = Text(f"Jarak: {dist_val:.1f}", font=FONT_CODE, font_size=16, color=color)
            dist_label.move_to(line.get_center() + UP * 0.25)
            return VGroup(line, dist_label)
            
        return line
