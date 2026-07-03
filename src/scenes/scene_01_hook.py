"""
[00:00 - 00:35] SCENE 1: HOOK (REVISI TOTAL - FULL PUTIH & BLACK-BLUE BG)
Perbaikan:
1. Latar belakang hitam dicampur biru (#0A1128).
2. Teks full putih (#FFFFFF), tidak ada warna kuning.
3. Ditambahkan animasi cursor mengetik nyata pada gelembung pertanyaan user.
4. Bug streaming kata per kata diperbaiki: tidak menggunakan invisible parent group,
   kata muncul satu per satu dengan posisi yang sudah diatur dengan tepat.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from manim import *
from src.constants import *
from src.components.chat_ui import ChatGPTUI
from src.utils.animations import create_glowing_surround_rect

def find_phrase_index(full_text: str, phrase: str) -> int:
    words = full_text.split()
    target = phrase.split()
    n = len(target)
    for i in range(len(words) - n + 1):
        if words[i:i + n] == target:
            return i
    raise ValueError(f"Frasa '{phrase}' tidak ditemukan.")

class HookScene(Scene):
    def construct(self):
        # Latar belakang hitam dicampur biru ala permintaan user (#0A1128)
        self.camera.background_color = DARK_BG

        # 1. Munculkan Antarmuka ChatGPT Mockup (Jelas dan kontras)
        chat_ui = ChatGPTUI(width=11.0, height=6.5)
        self.play(FadeIn(chat_ui, scale=0.95), run_time=TIME_NORMAL)
        self.wait(0.5)

        # 2. Animasi Cursor Mengetik Pertanyaan User ("Apa itu—")
        prompt_group, prompt_text, prompt_box = chat_ui.create_user_prompt("Apa itu ChatGPT dan bagaimana cara kerjanya?")
        
        # Munculkan gelembung kosong dulu
        self.play(FadeIn(prompt_box, shift=UP * 0.2), run_time=0.4)
        
        # Buat cursor putih di sebelah kiri teks
        cursor = Rectangle(width=0.08, height=0.35, fill_color="#FFFFFF", fill_opacity=1, stroke_width=0)
        cursor.next_to(prompt_text.get_left(), LEFT, buff=0.05)
        self.add(cursor)
        
        # Animasi mengetik: teks muncul sambil cursor bergerak ke kanan
        self.play(
            Write(prompt_text, run_time=1.5),
            cursor.animate.next_to(prompt_text.get_right(), RIGHT, buff=0.08).set_run_time(1.5)
        )
        self.play(FadeOut(cursor), run_time=0.3)
        self.wait(0.5)

        # 3. Jawaban AI ngalir kata demi kata secara real-time (FULL PUTIH #FFFFFF)
        response_text = (
            "ChatGPT sebenarnya tidak pernah tahu jawaban penuh dari awal. "
            "Dia hanya sangat jago menebak satu kata berikutnya. "
            "Terus, satu kata lagi. Terus, satu kata lagi. Berulang-ulang secepat kilat!"
        )
        ai_words = chat_ui.create_ai_response_words(response_text)

        # Animasi muncul kata per kata yang sebenarnya (tanpa invisible parent group)
        for word in ai_words:
            self.play(FadeIn(word, shift=UP * 0.05), run_time=0.06)

        self.wait(1.0)

        # 4. Highlight konsep utama dengan kotak putih/biru terang (tanpa warna kuning!)
        start_idx = find_phrase_index(response_text, "menebak satu kata berikutnya.")
        phrase_len = len("menebak satu kata berikutnya.".split())
        target_phrase = VGroup(*ai_words[start_idx:start_idx + phrase_len])

        # Kotak highlight warna putih (#FFFFFF)
        glow_rect = create_glowing_surround_rect(target_phrase, color="#FFFFFF", buff=0.1)
        self.play(Create(glow_rect), run_time=TIME_NORMAL)

        # Teks penekanan di atas UI (FULL PUTIH #FFFFFF)
        highlight_text = Text(
            "FOKUS TUNGGAL: Menebak Satu Kata Berikutnya!",
            font=FONT_PRIMARY,
            font_size=FONT_SIZE_BODY,
            color="#FFFFFF"
        ).to_edge(UP, buff=0.35)

        self.play(Write(highlight_text), run_time=TIME_NORMAL)
        self.wait(TIME_READING * 1.5)

        # 5. Transisi keluar untuk persiapan scene berikutnya
        self.play(
            FadeOut(glow_rect),
            FadeOut(chat_ui),
            FadeOut(ai_words),
            FadeOut(prompt_group),
            FadeOut(highlight_text),
            run_time=TIME_NORMAL
        )

if __name__ == "__main__":
    with tempconfig({"quality": "high_quality", "preview": True}):
        scene = HookScene()
        scene.render()