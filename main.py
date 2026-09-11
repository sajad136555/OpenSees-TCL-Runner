#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OpenSees TCL Runner - برنامه اجرای فایل‌های TCL
A beautiful and professional GUI application for running TCL files with OpenSees
"""

import sys
import os
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
