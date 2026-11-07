; اسکریپت Inno Setup برای ساخت نصب‌کنندهٔ ویندوز (بعد از اجرای build.bat)
[Setup]
AppName=نرم‌افزار آیین‌نامه ۲۸۰۰
AppVersion=5.0
AppPublisher=سجاد فروزنده
DefaultDirName={autopf}\Seismic2800
DefaultGroupName=Seismic 2800
OutputBaseFilename=Seismic2800_Setup
SetupIconFile=icon.ico
Compression=lzma2
[Files]
Source: "dist\Seismic2800.exe"; DestDir: "{app}"
[Icons]
Name: "{group}\نرم‌افزار ۲۸۰۰"; Filename: "{app}\Seismic2800.exe"
Name: "{autodesktop}\نرم‌افزار ۲۸۰۰"; Filename: "{app}\Seismic2800.exe"
