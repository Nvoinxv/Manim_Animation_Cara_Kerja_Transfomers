# Skrip Setup Virtual Environment & Instalasi Manim (Windows PowerShell)

$ENV_NAME = "myenv"

Write-Host "🚀 [1/3] Membuat Python Virtual Environment ($ENV_NAME)..." -ForegroundColor Cyan
python -m venv $ENV_NAME

Write-Host "🔗 [2/3] Mengaktifkan Virtual Environment..." -ForegroundColor Cyan
if (Test-Path "$ENV_NAME\Scripts\Activate.ps1") {
    . "$ENV_NAME\Scripts\Activate.ps1"
} else {
    Write-Host "❌ Gagal mengaktifkan environment. Pastikan script execution policy mengizinkan." -ForegroundColor Red
    exit
}

Write-Host "📦 [3/3] Menginstal dependensi Manim dari requirements.txt..." -ForegroundColor Cyan
python -m pip install --upgrade pip
pip install -r requirements.txt

Write-Host "`n🎉 Setup selesai! Untuk mengaktifkan environment di sesi terminal baru, jalankan:" -ForegroundColor Green
Write-Host "👉 .\$ENV_NAME\Scripts\activate" -ForegroundColor Yellow
