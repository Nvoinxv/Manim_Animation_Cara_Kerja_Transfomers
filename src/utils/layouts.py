"""
Utiliti tata letak (Layouts) untuk mengatur komponen visual geometri,
grafik probabilitas, dan sistem koordinat ruang vektor.
"""

from manim import *
from src.constants import *

def create_probability_bar_chart(candidates, probabilities, colors=None, width=5.0, height=3.0):
    """
    Membuat grafik batang horizontal (Horizontal Bar Chart) untuk menampilkan
    distRIBUTION probabilitas kata berikutnya ala mesin prediksi ChatGPT.
    
    Args:
        candidates (list[str]): Daftar kata kandidat (misal: ["Jakarta", "kucing", "meja"])
        probabilities (list[float]): Nilai probabilitas 0.0 - 1.0 (misal: [0.85, 0.05, 0.02])
        colors (list[str], optional): Warna masing-masing batang
    """
    if colors is None:
        colors = [GREEN_3B1B if i == 0 else MUTED_TEXT for i in range(len(candidates))]
        
    chart_group = VGroup()
    max_prob = max(probabilities) if probabilities else 1.0
    
    for i, (word, prob, col) in enumerate(zip(candidates, probabilities, colors)):
        row = VGroup()
        
        # Teks label kata
        label = Text(word, font=FONT_PRIMARY, font_size=FONT_SIZE_BODY, color=WHITE_TEXT)
        label.set_width(min(label.width, 1.8))
        
        # Batang probabilitas
        bar_max_width = width - 2.5
        bar_width = (prob / max_prob) * bar_max_width
        bar = RoundedRectangle(
            corner_radius=0.08,
            width=max(bar_width, 0.05),
            height=0.4,
            fill_color=col,
            fill_opacity=0.8,
            stroke_color=col,
            stroke_width=1
        )
        
        # Teks persentase
        pct_text = Text(f"{int(prob * 100)}%", font=FONT_CODE, font_size=FONT_SIZE_CAPTION, color=col)
        
        # Susun baris: Label -> Bar -> Persentase
        label.move_to(ORIGIN)
        bar.next_to(label, RIGHT, buff=0.3, aligned_edge=LEFT)
        # Geser bar agar sejajar kiri
        bar.align_to(label, UP)
        bar.set_y(label.get_y())
        pct_text.next_to(bar, RIGHT, buff=0.2)
        
        row.add(label, bar, pct_text)
        row.move_to(UP * (-i * 0.8))
        chart_group.add(row)
        
    # Rata kiri seluruh label
    left_x = min([row[0].get_left()[0] for row in chart_group])
    for row in chart_group:
        shift_x = left_x - row[0].get_left()[0]
        row[0].shift(RIGHT * shift_x)
        row[1].next_to(row[0], RIGHT, buff=0.3)
        row[2].next_to(row[1], RIGHT, buff=0.2)
        
    return chart_group

def create_vector_space_axes(dim=2, x_range=(-4, 4), y_range=(-3, 3), z_range=(-3, 3)):
    """
    Membuat sistem koordinat sumbu 2D atau 3D bergaya 3Blue1Brown
    untuk memvisualisasikan token embedding space.
    """
    if dim == 3:
        axes = ThreeDAxes(
            x_range=x_range,
            y_range=y_range,
            z_range=z_range,
            axis_config={"color": PANEL_BORDER, "stroke_width": 2, "include_tip": True},
            x_length=7,
            y_length=5,
            z_length=4
        )
    else:
        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            axis_config={"color": PANEL_BORDER, "stroke_width": 2, "include_tip": True},
            x_length=8,
            y_length=5
        )
    return axes
