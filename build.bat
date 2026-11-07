@echo off
chcp 65001 >nul
echo ===== ساخت نرم‌افزار ۲۸۰۰ =====
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
pyinstaller --noconfirm --onefile --windowed --name Seismic2800 --icon icon.ico --add-data "app;app" app.py
echo.
echo فایل نهایی: dist\Seismic2800.exe
pause
