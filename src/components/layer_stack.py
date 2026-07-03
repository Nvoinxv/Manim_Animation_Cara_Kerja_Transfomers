"""
Komponen visual untuk pengolahan berlapis-lapis (Layered Processing / Transformer Layers).
Menampilkan tumpukan lapisan transparan dari bawah ke atas di mana setiap layer
memperkaya pemahaman model dari sintaksis sederhana hingga abstraksi logika sebab-akibat.
"""

from manim import *
from src.constants import *

class LayerStack(VGroup):
    """
    Tumpukan kotak transparan 2D/3D isometrik yang melambangkan
    lapisan-lapisan (Layers) dalam arsitektur Transformer neural network.
    """
    def __init__(self, num_layers=4, layer_width=7.0, layer_height=1.2, spacing=1.6, **kwargs):
        super().__init__(**kwargs)
        self.num_layers = num_layers
        self.layer_width = layer_width
        self.layer_height = layer_height
        self.spacing = spacing
        
        self.layers = VGroup()
        self.labels = VGroup()
        self.connectors = VGroup()
        
        layer_names = [
            "Layer 1: Sintaksis & Tata Bahasa (Kata Benda/Kerja)",
            "Layer 12: Hubungan Konteks Dekat",
            "Layer 48: Maksud Tersirat & Nada Kalimat",
            "Layer 96: Logika Sebab-Akibat & Abstraksi Tinggi"
        ]
        
        layer_colors = [BLUE_DARK, BLUE_3B1B, TEAL_3B1B, PURPLE_3B1B]
        
        for i in range(num_layers):
            col = layer_colors[i % len(layer_colors)]
            name = layer_names[i] if i < len(layer_names) else f"Transformer Layer #{i+1}"
            
            # Kotak Layer
            box = RoundedRectangle(
                corner_radius=0.15,
                width=layer_width,
                height=layer_height,
                fill_color=col,
                fill_opacity=0.25,
                stroke_color=col,
                stroke_width=2
            )
            box.move_to(UP * (i * spacing))
            
            # Label Layer
            label = Text(name, font=FONT_PRIMARY, font_size=20, color=WHITE_TEXT)
            label.move_to(box.get_center())
            
            self.layers.add(box)
            self.labels.add(label)
            
            # Panah koneksi dari layer bawah ke atas
            if i > 0:
                prev_box = self.layers[i-1]
                arrow = Arrow(
                    prev_box.get_top(),
                    box.get_bottom(),
                    color=MUTED_TEXT,
                    stroke_width=2,
                    buff=0.1,
                    max_tip_length_to_length_ratio=0.2
                )
                self.connectors.add(arrow)
                
        self.add(self.layers, self.labels, self.connectors)
        self.move_to(ORIGIN)
        
    def animate_data_flow(self, token_dot: Dot, start_color=BLUE_3B1B, end_color=PURPLE_3B1B, run_time=3.0):
        """
        Mengembalikan animasi pergerakan titik data/token yang naik melewati setiap layer,
        berubah warna dan posisinya sebagai simbol pemaknaan yang makin kaya dan abstrak.
        """
        animations = []
        path_points = [layer.get_center() for layer in self.layers]
        
        # Posisikan dot di bawah layer pertama
        token_dot.move_to(path_points[0] + DOWN * 1.5)
        token_dot.set_color(start_color)
        
        steps = len(path_points)
        for i, pt in enumerate(path_points):
            alpha = (i + 1) / steps
            interp_color = interpolate_color(start_color, end_color, alpha)
            
            # Animasi naik ke tengah layer dan berubah warna
            step_anim = token_dot.animate.move_to(pt).set_color(interp_color).scale(1.1)
            animations.append(step_anim)
            
            # Efek pulse pada layer saat dilewati data
            layer_pulse = self.layers[i].animate.set_fill(opacity=0.6).set_run_time(0.3)
            layer_restore = self.layers[i].animate.set_fill(opacity=0.25).set_run_time(0.3)
            animations.append(Succession(layer_pulse, layer_restore))
            
        return Succession(*animations)
