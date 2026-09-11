# -*- coding: utf-8 -*-
"""
Stye Sheets for the application
"""

DARK_STYLESHEET = """
QMainWindow {
    background-color: #1e1e2e;
}

QWidget {
    background-color: #1e1e2e;
    color: #e0e0e0;
}

QPushButton {
    background-color: #0ea5e9;
    color: white;
    border: none;
    border-radius: 6px;
    padding: 10px 20px;
    font-size: 14px;
    font-weight: bold;
    min-height: 40px;
}

QPushButton:hover {
    background-color: #0284c7;
}

QPushButton:pressed {
    background-color: #0369a1;
}

QPushButton#btnPrimary {
    background-color: #10b981;
}

QPushButton#btnPrimary:hover {
    background-color: #059669;
}

QPushButton#btnDanger {
    background-color: #ef4444;
}

QPushButton#btnDanger:hover {
    background-color: #dc2626;
}

QLabel {
    color: #e0e0e0;
}

QLabel#titleLabel {
    font-size: 24px;
    font-weight: bold;
    color: #0ea5e9;
    margin: 10px;
}

QLabel#subtitleLabel {
    font-size: 14px;
    color: #9ca3af;
    margin: 5px;
}

QLineEdit {
    background-color: #2d2d3d;
    color: #e0e0e0;
    border: 2px solid #3d3d4d;
    border-radius: 6px;
    padding: 8px;
    font-size: 13px;
}

QLineEdit:focus {
    border: 2px solid #0ea5e9;
}

QTextEdit {
    background-color: #2d2d3d;
    color: #e0e0e0;
    border: 2px solid #3d3d4d;
    border-radius: 6px;
    padding: 8px;
    font-size: 12px;
    font-family: 'Courier New';
}

QTextEdit:focus {
    border: 2px solid #0ea5e9;
}

QListWidget {
    background-color: #2d2d3d;
    color: #e0e0e0;
    border: 2px solid #3d3d4d;
    border-radius: 6px;
}

QListWidget::item {
    padding: 8px;
}

QListWidget::item:hover {
    background-color: #3d3d4d;
}

QListWidget::item:selected {
    background-color: #0ea5e9;
    color: white;
}

QGroupBox {
    color: #e0e0e0;
    border: 2px solid #3d3d4d;
    border-radius: 6px;
    margin-top: 10px;
    padding-top: 10px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 3px 0 3px;
}

QTabBar::tab {
    background-color: #2d2d3d;
    color: #9ca3af;
    padding: 8px 20px;
    border: none;
}

QTabBar::tab:selected {
    background-color: #0ea5e9;
    color: white;
}

QTabBar::tab:hover {
    background-color: #3d3d4d;
}

QComboBox {
    background-color: #2d2d3d;
    color: #e0e0e0;
    border: 2px solid #3d3d4d;
    border-radius: 6px;
    padding: 6px;
}

QComboBox::drop-down {
    border: none;
}

QComboBox::down-arrow {
    image: url('down-arrow.png');
}

QCheckBox {
    color: #e0e0e0;
    spacing: 5px;
}

QCheckBox::indicator {
    width: 18px;
    height: 18px;
}

QCheckBox::indicator:unchecked {
    background-color: #2d2d3d;
    border: 2px solid #3d3d4d;
    border-radius: 3px;
}

QCheckBox::indicator:checked {
    background-color: #0ea5e9;
    border: 2px solid #0ea5e9;
    border-radius: 3px;
}

QProgressBar {
    background-color: #2d2d3d;
    border: 2px solid #3d3d4d;
    border-radius: 6px;
    text-align: center;
    color: #e0e0e0;
}

QProgressBar::chunk {
    background-color: #0ea5e9;
    border-radius: 4px;
}

QStatusBar {
    background-color: #2d2d3d;
    color: #9ca3af;
    border-top: 1px solid #3d3d4d;
}

QMenuBar {
    background-color: #1e1e2e;
    color: #e0e0e0;
}

QMenuBar::item:selected {
    background-color: #0ea5e9;
}

QMenu {
    background-color: #2d2d3d;
    color: #e0e0e0;
    border: 1px solid #3d3d4d;
}

QMenu::item:selected {
    background-color: #0ea5e9;
    color: white;
}

QHeaderView::section {
    background-color: #2d2d3d;
    color: #e0e0e0;
    padding: 5px;
    border: 1px solid #3d3d4d;
}

QTableWidget {
    background-color: #2d2d3d;
    color: #e0e0e0;
    gridline-color: #3d3d4d;
    border: 2px solid #3d3d4d;
    border-radius: 6px;
}

QTableWidget::item {
    padding: 5px;
}

QTableWidget::item:selected {
    background-color: #0ea5e9;
}
"""

LIGHT_STYLESHEET = """
QMainWindow {
    background-color: #f8fafc;
}

QWidget {
    background-color: #f8fafc;
    color: #1e293b;
}

QPushButton {
    background-color: #0ea5e9;
    color: white;
    border: none;
    border-radius: 6px;
    padding: 10px 20px;
    font-size: 14px;
    font-weight: bold;
    min-height: 40px;
}

QPushButton:hover {
    background-color: #0284c7;
}

QPushButton:pressed {
    background-color: #0369a1;
}

QPushButton#btnPrimary {
    background-color: #10b981;
}

QPushButton#btnPrimary:hover {
    background-color: #059669;
}

QPushButton#btnDanger {
    background-color: #ef4444;
}

QPushButton#btnDanger:hover {
    background-color: #dc2626;
}

QLabel {
    color: #1e293b;
}

QLabel#titleLabel {
    font-size: 24px;
    font-weight: bold;
    color: #0ea5e9;
    margin: 10px;
}

QLabel#subtitleLabel {
    font-size: 14px;
    color: #64748b;
    margin: 5px;
}

QLineEdit {
    background-color: white;
    color: #1e293b;
    border: 2px solid #e2e8f0;
    border-radius: 6px;
    padding: 8px;
    font-size: 13px;
}

QLineEdit:focus {
    border: 2px solid #0ea5e9;
}

QTextEdit {
    background-color: white;
    color: #1e293b;
    border: 2px solid #e2e8f0;
    border-radius: 6px;
    padding: 8px;
    font-size: 12px;
    font-family: 'Courier New';
}

QTextEdit:focus {
    border: 2px solid #0ea5e9;
}

QListWidget {
    background-color: white;
    color: #1e293b;
    border: 2px solid #e2e8f0;
    border-radius: 6px;
}

QListWidget::item {
    padding: 8px;
}

QListWidget::item:hover {
    background-color: #f1f5f9;
}

QListWidget::item:selected {
    background-color: #0ea5e9;
    color: white;
}

QGroupBox {
    color: #1e293b;
    border: 2px solid #e2e8f0;
    border-radius: 6px;
    margin-top: 10px;
    padding-top: 10px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 3px 0 3px;
}

QTabBar::tab {
    background-color: #f1f5f9;
    color: #64748b;
    padding: 8px 20px;
    border: none;
}

QTabBar::tab:selected {
    background-color: #0ea5e9;
    color: white;
}

QTabBar::tab:hover {
    background-color: #e2e8f0;
}

QComboBox {
    background-color: white;
    color: #1e293b;
    border: 2px solid #e2e8f0;
    border-radius: 6px;
    padding: 6px;
}

QCheckBox {
    color: #1e293b;
    spacing: 5px;
}

QCheckBox::indicator {
    width: 18px;
    height: 18px;
}

QCheckBox::indicator:unchecked {
    background-color: white;
    border: 2px solid #e2e8f0;
    border-radius: 3px;
}

QCheckBox::indicator:checked {
    background-color: #0ea5e9;
    border: 2px solid #0ea5e9;
    border-radius: 3px;
}

QProgressBar {
    background-color: #f1f5f9;
    border: 2px solid #e2e8f0;
    border-radius: 6px;
    text-align: center;
    color: #1e293b;
}

QProgressBar::chunk {
    background-color: #0ea5e9;
    border-radius: 4px;
}

QStatusBar {
    background-color: #f1f5f9;
    color: #64748b;
    border-top: 1px solid #e2e8f0;
}

QMenuBar {
    background-color: #f8fafc;
    color: #1e293b;
}

QMenuBar::item:selected {
    background-color: #0ea5e9;
    color: white;
}

QMenu {
    background-color: white;
    color: #1e293b;
    border: 1px solid #e2e8f0;
}

QMenu::item:selected {
    background-color: #0ea5e9;
    color: white;
}
"""
