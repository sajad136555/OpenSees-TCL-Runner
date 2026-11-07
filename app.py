# -*- coding: utf-8 -*-
"""نرم‌افزار آیین‌نامه ۲۸۰۰ ویرایش پنجم — نسخهٔ دسکتاپ (طراح و سازنده: سجاد فروزنده)"""
import base64, os, sys
import webview

def res(p):
    base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, p)

class Api:
    def save_file(self, filename, b64):
        w = webview.windows[0]
        r = w.create_file_dialog(webview.SAVE_DIALOG, save_filename=filename)
        if not r:
            return False
        path = r if isinstance(r, str) else r[0]
        with open(path, 'wb') as f:
            f.write(base64.b64decode(b64))
        return True

def main():
    webview.create_window(
        'نرم‌افزار آیین‌نامه ۲۸۰۰ — ویرایش پنجم  |  سجاد فروزنده',
        res(os.path.join('app', 'index.html')),
        js_api=Api(), width=1360, height=860, min_size=(1000, 650), text_select=True,
        background_color='#0a2260')
    store = os.path.join(os.environ.get('APPDATA', os.path.expanduser('~')), 'Seismic2800')
    webview.start(private_mode=False, storage_path=store)

if __name__ == '__main__':
    main()
