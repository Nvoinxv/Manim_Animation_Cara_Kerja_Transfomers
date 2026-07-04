"""
[00:00 - 00:35] SCENE 1: HOOK (REVISI - FIX CRASH)
Perbaikan dari versi sebelumnya:
1. CRASH FIX: create_user_prompt() cuma return 1 VGroup (bubble+text),
   bukan 3 nilai. Sekarang manggilnya pakai return_parts=True (lihat
   chat_ui_patch.py) supaya benar-benar dapat 3 nilai terpisah:
   group, bubble, text.
2. CRASH FIX: create_ai_response_words() me-return TUPLE (word_mobjects, lines).
   Kode sebelumnya nyimpen tuple itu langsung ke `ai_words` lalu iterasi
   di atasnya -- itu iterasi 2 grup besar, bukan kata satu-satu, dan bikin
   FadeOut(ai_words) di akhir error karena tuple bukan Mobject.
   Sekarang di-unpack dengan benar: `ai_words, ai_lines = ...`.
3. Karena bug #1 dan #2 di atas nge-crash construct() SEBELUM chat UI,
   cursor mengetik, dan streaming kata sempat jalan -- itu penyebab video
   akhir cuma nampilin highlight_text (fragment terakhir yang sempat
   ke-cache sebelum scene lain error / video lama yang stale ditonton ulang).
   SARAN: selalu cek traceback di terminal setiap render, jangan cuma
   nonton video hasilnya -- traceback langsung nunjuk baris yang crash.
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
    raise ValueError(f"Frasa '{phrase}' tidak ditemukan di response_text.")


class HookScene(Scene):
    def construct(self):
        # CATATAN: pastikan DARK_BG di constants.py memang sudah #0A1128.
        # Kalau belum, ganti di constants.py -- bukan di sini -- supaya
        # konsisten dipakai scene lain juga.
        self.camera.background_color = DARK_BG

        # 1. Munculkan Antarmuka ChatGPT Mockup
        chat_ui = ChatGPTUI(width=11.0, height=6.5)
        self.play(FadeIn(chat_ui, scale=0.95), run_time=TIME_NORMAL)
        self.wait(0.5)

        # 2. Animasi Cursor Mengetik Pertanyaan User
        # FIX: return_parts=True supaya benar-benar dapat 3 nilai terpisah
        prompt_group, prompt_bubble, prompt_text = chat_ui.create_user_prompt(
            "Apa itu ChatGPT dan bagaimana cara kerjanya?",
            return_parts=True
        )

        # Munculkan gelembung kosong dulu (teks belum ditulis)
        prompt_text.set_opacity(0)
        self.play(FadeIn(prompt_bubble, shift=UP * 0.2), run_time=0.4)

        # Cursor putih di ujung kiri posisi akhir teks
        cursor = Rectangle(width=0.08, height=0.35, fill_color="#FFFFFF", fill_opacity=1, stroke_width=0)
        cursor.next_to(prompt_text.get_left(), LEFT, buff=0.05)
        self.add(cursor)

        prompt_text.set_opacity(1)  # posisi/geometri sudah benar, tinggal di-reveal via Write
        self.play(
            Write(prompt_text, run_time=1.5),
            cursor.animate.next_to(prompt_text.get_right(), RIGHT, buff=0.08).set_run_time(1.5)
        )
        self.play(FadeOut(cursor), run_time=0.3)
        self.wait(0.5)

        # 3. Jawaban AI ngalir kata demi kata
        response_text = (
            "ChatGPT sebenarnya tidak pernah tahu jawaban penuh dari awal. "
            "Dia hanya sangat jago menebak satu kata berikutnya. "
            "Terus, satu kata lagi. Terus, satu kata lagi. Berulang-ulang secepat kilat!"
        )
        # FIX: unpack tuple dengan benar -- ai_words = daftar kata individual,
        # ai_lines = grup baris (dipakai kalau butuh FadeOut semuanya sekaligus)
        ai_words, ai_lines = chat_ui.create_ai_response_words(response_text)

        for word in ai_words:
            self.play(FadeIn(word, shift=UP * 0.05), run_time=0.06)

        self.wait(1.0)

        # 4. Highlight konsep utama, warna putih
        start_idx = find_phrase_index(response_text, "menebak satu kata berikutnya.")
        phrase_len = len("menebak satu kata berikutnya.".split())
        target_phrase = VGroup(*ai_words[start_idx:start_idx + phrase_len])

        glow_rect = create_glowing_surround_rect(target_phrase, color="#FFFFFF", buff=0.1)
        self.play(Create(glow_rect), run_time=TIME_NORMAL)

        highlight_text = Text(
            "FOKUS TUNGGAL: Menebak Satu Kata Berikutnya!",
            font=FONT_PRIMARY,
            font_size=FONT_SIZE_BODY,
            color="#FFFFFF"
        ).to_edge(UP, buff=0.35)

        self.play(Write(highlight_text), run_time=TIME_NORMAL)
        self.wait(TIME_READING * 1.5)

        # 5. Transisi keluar -- semua variabel di sini sekarang Mobject asli,
        # bukan tuple, jadi FadeOut tidak akan error
        self.play(
            FadeOut(glow_rect),
            FadeOut(chat_ui),
            FadeOut(ai_lines),
            FadeOut(prompt_group),
            FadeOut(highlight_text),
            run_time=TIME_NORMAL
        )


if __name__ == "__main__":
    with tempconfig({"quality": "high_quality", "preview": True, "disable_caching": True}):
        scene = HookScene()
        scene.render()