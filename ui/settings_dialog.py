# -*- coding: utf-8 -*-
"""
Settings dialog for OpenSees TCL Runner
"""

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QFileDialog, QMessageBox, QComboBox, QGroupBox
)
from PyQt6.QtCore import Qt

from core.config import config

class SettingsDialog(QDialog):
    """Settings dialog"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("تنظیمات")
        self.setGeometry(200, 200, 600, 400)
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the dialog UI"""
        layout = QVBoxLayout()
        
        # OpenSees Path section
        opensees_group = QGroupBox("مسیر OpenSees")
        opensees_layout = QHBoxLayout()
        
        opensees_label = QLabel("مسیر:")
        self.opensees_input = QLineEdit()
        self.opensees_input.setText(config.get('opensees_path', config.DEFAULT_OPENSEES_PATH))
        self.opensees_input.setReadOnly(True)
        
        browse_opensees_btn = QPushButton("مرور...")
        browse_opensees_btn.clicked.connect(self.browse_opensees)
        
        opensees_layout.addWidget(opensees_label)
        opensees_layout.addWidget(self.opensees_input)
        opensees_layout.addWidget(browse_opensees_btn)
        opensees_group.setLayout(opensees_layout)
        layout.addWidget(opensees_group)
        
        # Initial Directory section
        initial_group = QGroupBox("مسیر اولیه")
        initial_layout = QHBoxLayout()
        
        initial_label = QLabel("مسیر:")
        self.initial_input = QLineEdit()
        self.initial_input.setText(config.get('initial_dir', config.DEFAULT_INITIAL_DIR))
        self.initial_input.setReadOnly(True)
        
        browse_initial_btn = QPushButton("مرور...")
        browse_initial_btn.clicked.connect(self.browse_initial_dir)
        
        initial_layout.addWidget(initial_label)
        initial_layout.addWidget(self.initial_input)
        initial_layout.addWidget(browse_initial_btn)
        initial_group.setLayout(initial_layout)
        layout.addWidget(initial_group)
        
        # Theme section
        theme_group = QGroupBox("تم")
        theme_layout = QHBoxLayout()
        
        theme_label = QLabel("انتخاب تم:")
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["تاریک", "روشن"])
        current_theme = config.get('theme', 'dark')
        self.theme_combo.setCurrentIndex(0 if current_theme == 'dark' else 1)
        
        theme_layout.addWidget(theme_label)
        theme_layout.addWidget(self.theme_combo)
        theme_layout.addStretch()
        theme_group.setLayout(theme_layout)
        layout.addWidget(theme_group)
        
        layout.addStretch()
        
        # Buttons
        button_layout = QHBoxLayout()
        
        ok_btn = QPushButton("تأیید")
        ok_btn.clicked.connect(self.accept)
        
        cancel_btn = QPushButton("لغو")
        cancel_btn.clicked.connect(self.reject)
        
        reset_btn = QPushButton("بازنشانی پیش‌فرض")
        reset_btn.clicked.connect(self.reset_defaults)
        
        button_layout.addWidget(reset_btn)
        button_layout.addStretch()
        button_layout.addWidget(ok_btn)
        button_layout.addWidget(cancel_btn)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def browse_opensees(self):
        """Browse for OpenSees executable"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "انتخاب OpenSees",
            "C:\\",
            "Executable Files (*.exe);;All Files (*)"
        )
        
        if file_path:
            self.opensees_input.setText(file_path)
    
    def browse_initial_dir(self):
        """Browse for initial directory"""
        dir_path = QFileDialog.getExistingDirectory(
            self,
            "انتخاب مسیر اولیه",
            "H:\\"
        )
        
        if dir_path:
            self.initial_input.setText(dir_path)
    
    def reset_defaults(self):
        """Reset to default settings"""
        reply = QMessageBox.question(
            self,
            "تأیید",
            "آیا مطمئن هستید؟"
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.opensees_input.setText(config.DEFAULT_OPENSEES_PATH)
            self.initial_input.setText(config.DEFAULT_INITIAL_DIR)
            self.theme_combo.setCurrentIndex(0)
    
    def accept(self):
        """Save settings and close"""
        config.set('opensees_path', self.opensees_input.text())
        config.set('initial_dir', self.initial_input.text())
        
        theme = 'dark' if self.theme_combo.currentIndex() == 0 else 'light'
        config.set('theme', theme)
        
        config.save_config()
        super().accept()
