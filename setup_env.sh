#!/usr/bin/env bash
# Skrip Setup Virtual Environment & Instalasi Manim (Git Bash / Linux / macOS)

ENV_NAME="myenv"

echo "🚀 [1/3] Membuat Python Virtual Environment ($ENV_NAME)..."
python3 -m venv $ENV_NAME || python -m venv $ENV_NAME

echo "🔗 [2/3] Mengaktifkan Virtual Environment..."
source $ENV_NAME/bin/activate

echo "📦 [3/3] Menginstal dependensi Manim dari requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "🎉 Setup selesai! Untuk mengaktifkan environment di sesi terminal baru, jalankan:"
echo "👉 source $ENV_NAME/bin/activate"
