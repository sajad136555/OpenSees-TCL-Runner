' اجرای نرم‌افزار در پنجرهٔ مستقل (بدون نوار آدرس) با Microsoft Edge — بدون نیاز به پایتون یا نصب
Set sh = CreateObject("WScript.Shell")
Set fs = CreateObject("Scripting.FileSystemObject")
p = Replace(Replace(fs.GetParentFolderName(WScript.ScriptFullName), "\", "/"), " ", "%20")
sh.Run "msedge --app=""file:///" & p & "/app/index.html"" --window-size=1360,860", 1, False
