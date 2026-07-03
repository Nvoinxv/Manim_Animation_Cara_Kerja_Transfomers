"""
[00:00 - 00:35] SCENE 1: HOOK
Fokus Visual: Layar kosong. Muncul cursor ngetik "Apa itu—" terus muncul jawaban ChatGPT
ngalir kata demi kata secara real-time. Menyorot bahwa ChatGPT tidak tahu jawaban penuh dari awal,
melainkan menebak satu kata berikutnya secara berulang-ulang secepat kilat.
"""

from manim import *
from src.constants import *
from src.components.chat_ui import ChatGPTUI
from src.utils.animations import TypewriterText, create_glowing_surround_rect

class HookScene(Scene):
    def construct(self):
        self.camera.background_color = DARK_BG
        
        # 1. Munculkan Antarmuka ChatGPT Mockup
        chat_ui = ChatGPTUI(width=11.0, height=6.5)
        self.play(FadeIn(chat_ui, scale=0.9), run_time=TIME_NORMAL)
        self.wait(0.5)
        
        # 2. Cursor mengetik pertanyaan user ("Apa itu—")
        prompt_bubble = chat_ui.create_user_prompt("Apa itu ChatGPT dan bagaimana cara kerjanya?")
        self.play(FadeIn(prompt_bubble, shift=UP * 0.3), run_time=TIME_NORMAL)
        self.wait(0.5)
        
        # 3. Jawaban AI ngalir kata demi kata secara real-time
        ai_words, ai_lines = chat_ui.create_ai_response_words(
            "ChatGPT sebenarnya tidak pernah tahu jawaban penuh dari awal. "
            "Dia hanya sangat jago menebak satu kata berikutnya. "
            "Terus, satu kata lagi. Terus, satu kata lagi. Berulang-ulang secepat kilat!"
        )
        
        # Animasi muncul kata per kata (Streaming / Typewriter effect)
        self.play(FadeIn(ai_lines), run_time=0.1)
        for word in ai_words:
            self.play(FadeIn(word, shift=UP * 0.1), run_time=0.08)
            
        self.wait(1.0)
        
        # 4. Highlight konsep utama: "menebak satu kata berikutnya"
        target_phrase = VGroup(*ai_words[8:12]) # "menebak satu kata berikutnya."
        glow_rect = create_glowing_surround_rect(target_phrase, color=YELLOW_3B1B, buff=0.1)
        
        self.play(Create(glow_rect), run_time=TIME_NORMAL)
        
        # Teks penjelasan penekanan di atas UI
        highlight_text = Text(
            "FOKUS TUNGGAL: Menebak Satu Kata Berikutnya!",
            font=FONT_PRIMARY,
            font_size=FONT_SIZE_BODY,
            color=YELLOW_3B1B
        ).to_edge(UP, buff=0.4)
        
        self.play(Write(highlight_text), run_time=TIME_NORMAL)
        self.wait(TIME_READING)
        
        # 5. Transisi keluar untuk persiapan scene berikutnya
        self.play(
            FadeOut(glow_rect),
            FadeOut(chat_ui),
            FadeOut(highlight_text),
            run_time=TIME_NORMAL
        )
