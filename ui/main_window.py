# -*- coding: utf-8 -*-
"""
Main window for OpenSees TCL Runner
"""

import os
from pathlib import Path
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QLineEdit, QFileDialog, QTextEdit, QTabWidget,
    QListWidget, QListWidgetItem, QGroupBox, QComboBox,
    QMessageBox, QProgressBar, QSplitter, QHeaderView, QTableWidget, QTableWidgetItem
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal, QSize
from PyQt6.QtGui import QIcon, QColor, QFont, QPixmap
from PyQt6.QtCore import QTimer

from core.config import config
from core.runner import TCLRunner
from ui.styles import DARK_STYLESHEET, LIGHT_STYLESHEET

class RunnerThread(QThread):
    """Thread for running TCL files"""
    finished = pyqtSignal(bool, str, str)  # success, output, error
    
    def __init__(self, runner: TCLRunner, file_path: str):
        super().__init__()
        self.runner = runner
        self.file_path = file_path
    
    def run(self):
        success, output, error = self.runner.run_file(self.file_path)
        self.finished.emit(success, output, error)

class MainWindow(QMainWindow):
    """Main application window"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenSees TCL Runner - برنامه اجرای فایل های TCL")
        self.setGeometry(100, 100, 1200, 800)
        
        # Set window icon
        self.setWindowIcon(self.create_icon())
        
        # Initialize runner
        opensees_path = config.get('opensees_path', config.DEFAULT_OPENSEES_PATH)
        self.runner = TCLRunner(opensees_path)
        self.runner_thread = None
        
        # Current selected file
        self.current_file = None
        self.running = False
        
        # Setup UI
        self.setup_ui()
        self.apply_theme()
        self.load_recent_files()
        
        # Check OpenSees availability
        if not self.runner.is_opensees_available():
            QMessageBox.warning(
                self,
                "تهذیر",
                f"OpenSees در مسیر {opensees_path} یافت نشد.\nلطفا تنظیمات را بررسی کنید."
            )
    
    def setup_ui(self):
        """Setup the user interface"""
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Header
        header_layout = QHBoxLayout()
        title_label = QLabel("OpenSees TCL Runner")
        title_label.setObjectName("titleLabel")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title_label.setFont(title_font)
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        
        # Theme toggle button
        self.theme_btn = QPushButton("🌙 تیره")
        self.theme_btn.clicked.connect(self.toggle_theme)
        self.theme_btn.setMaximumWidth(100)
        header_layout.addWidget(self.theme_btn)
        
        # Settings button
        settings_btn = QPushButton("⚙️ تنظیمات")
        settings_btn.clicked.connect(self.open_settings)
        settings_btn.setMaximumWidth(100)
        header_layout.addWidget(settings_btn)
        
        main_layout.addLayout(header_layout)
        
        # Separator
        sep1 = QLabel()
        sep1.setStyleSheet("border-top: 2px solid #3d3d4d;" if config.get('theme') == 'dark' else "border-top: 2px solid #e2e8f0;")
        main_layout.addWidget(sep1)
        
        # File selection section
        file_section = QGroupBox("انتخاب فایل")
        file_layout = QHBoxLayout()
        
        self.file_path_input = QLineEdit()
        self.file_path_input.setPlaceholderText("مسیر فایل TCL...")
        self.file_path_input.setReadOnly(True)
        file_layout.addWidget(self.file_path_input)
        
        browse_btn = QPushButton("📁 مرور")
        browse_btn.clicked.connect(self.browse_file)
        browse_btn.setMaximumWidth(100)
        file_layout.addWidget(browse_btn)
        
        clear_btn = QPushButton("✕ پاک کن")
        clear_btn.clicked.connect(self.clear_file)
        clear_btn.setMaximumWidth(100)
        file_layout.addWidget(clear_btn)
        
        file_section.setLayout(file_layout)
        main_layout.addWidget(file_section)
        
        # File info section
        info_section = QGroupBox("اطلاعات فایل")
        info_layout = QHBoxLayout()
        
        self.info_name = QLabel("نام: -")
        self.info_size = QLabel("اندازه: -")
        self.info_lines = QLabel("خطوط: -")
        self.info_modified = QLabel("تغییر: -")
        
        info_layout.addWidget(self.info_name)
        info_layout.addWidget(self.info_size)
        info_layout.addWidget(self.info_lines)
        info_layout.addWidget(self.info_modified)
        info_layout.addStretch()
        
        info_section.setLayout(info_layout)
        main_layout.addWidget(info_section)
        
        # Tabs
        tabs = QTabWidget()
        
        # Output tab
        output_layout = QVBoxLayout()
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setFont(QFont("Courier", 10))
        output_layout.addWidget(self.output_text)
        
        # Run controls
        controls_layout = QHBoxLayout()
        
        self.run_btn = QPushButton("▶ اجرا")
        self.run_btn.setObjectName("btnPrimary")
        self.run_btn.clicked.connect(self.run_file)
        self.run_btn.setMinimumHeight(45)
        controls_layout.addWidget(self.run_btn)
        
        self.stop_btn = QPushButton("⏹ توقف")
        self.stop_btn.setObjectName("btnDanger")
        self.stop_btn.clicked.connect(self.stop_run)
        self.stop_btn.setMinimumHeight(45)
        self.stop_btn.setEnabled(False)
        controls_layout.addWidget(self.stop_btn)
        
        save_output_btn = QPushButton("💾 ذخیره خروجی")
        save_output_btn.clicked.connect(self.save_output)
        save_output_btn.setMinimumHeight(45)
        controls_layout.addWidget(save_output_btn)
        
        clear_output_btn = QPushButton("🗑️ پاک کن")
        clear_output_btn.clicked.connect(lambda: self.output_text.clear())
        clear_output_btn.setMinimumHeight(45)
        controls_layout.addWidget(clear_output_btn)
        
        output_layout.addLayout(controls_layout)
        
        output_widget = QWidget()
        output_widget.setLayout(output_layout)
        tabs.addTab(output_widget, "خروجی")
        
        # Recent files tab
        recent_layout = QVBoxLayout()
        self.recent_list = QListWidget()
        self.recent_list.itemClicked.connect(self.on_recent_file_clicked)
        recent_layout.addWidget(QLabel("فایل های اخیر:"))
        recent_layout.addWidget(self.recent_list)
        
        recent_buttons = QHBoxLayout()
        open_recent_btn = QPushButton("📂 باز کن")
        open_recent_btn.clicked.connect(self.open_recent_file)
        recent_buttons.addWidget(open_recent_btn)
        
        clear_recent_btn = QPushButton("🗑️ پاک کن")
        clear_recent_btn.clicked.connect(self.clear_recent_files)
        recent_buttons.addWidget(clear_recent_btn)
        
        recent_buttons.addStretch()
        recent_layout.addLayout(recent_buttons)
        
        recent_widget = QWidget()
        recent_widget.setLayout(recent_layout)
        tabs.addTab(recent_widget, "اخیر")
        
        # Progress bar
        progress_layout = QVBoxLayout()
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setMaximum(0)  # Busy indicator
        progress_layout.addWidget(self.progress_bar)
        
        progress_widget = QWidget()
        progress_widget.setLayout(progress_layout)
        
        main_layout.addWidget(tabs)
        main_layout.addWidget(progress_widget)
        
        # Status bar
        self.statusBar().showMessage("آماده")
    
    def browse_file(self):
        """Browse and select a TCL file"""
        initial_dir = config.get('initial_dir', config.DEFAULT_INITIAL_DIR)
        
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "انتخاب فایل TCL",
            initial_dir,
            "TCL Files (*.tcl);;All Files (*)"
        )
        
        if file_path:
            self.set_file(file_path)
    
    def set_file(self, file_path: str):
        """Set the current file"""
        if os.path.isfile(file_path):
            self.current_file = file_path
            self.file_path_input.setText(file_path)
            
            # Update file info
            info = self.runner.get_file_info(file_path)
            self.info_name.setText(f"نام: {info.get('name', '-')}")
            self.info_size.setText(f"اندازه: {info.get('size_human', '-')}")
            self.info_lines.setText(f"خطوط: {info.get('lines', '-')}")
            self.info_modified.setText(f"تغییر: {info.get('modified', '-')}")
            
            # Add to recent files
            config.add_recent_file(file_path)
            self.load_recent_files()
            
            self.statusBar().showMessage(f"فایل انتخاب شد: {file_path}")
        else:
            QMessageBox.warning(self, "خطا", "فایل یافت نشد")
    
    def clear_file(self):
        """Clear the current file"""
        self.current_file = None
        self.file_path_input.clear()
        self.info_name.setText("نام: -")
        self.info_size.setText("اندازه: -")
        self.info_lines.setText("خطوط: -")
        self.info_modified.setText("تغییر: -")
        self.statusBar().showMessage("فایلی انتخاب نشده")
    
    def run_file(self):
        """Run the selected TCL file"""
        if not self.current_file:
            QMessageBox.warning(self, "خطا", "لطفا ابتدا یک فایل انتخاب کنید")
            return
        
        if not self.runner.is_opensees_available():
            QMessageBox.critical(
                self,
                "خطا",
                "OpenSees در دسترسی نیست. لطفا تنظیمات را بررسی کنید."
            )
            return
        
        self.running = True
        self.run_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        self.progress_bar.setVisible(True)
        self.statusBar().showMessage("در حال اجرا...")
        
        # Clear previous output
        self.output_text.clear()
        
        # Run in thread
        self.runner_thread = RunnerThread(self.runner, self.current_file)
        self.runner_thread.finished.connect(self.on_run_finished)
        self.runner_thread.start()
    
    def on_run_finished(self, success: bool, output: str, error: str):
        """Handle run finished"""
        self.running = False
        self.run_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        self.progress_bar.setVisible(False)
        
        # Display output
        if output:
            self.output_text.setText(output)
        
        if error:
            error_msg = f"\n\n{'='*60}\n✘ خطاها:\n{'='*60}\n{error}"
            self.output_text.append(error_msg)
        
        if success:
            self.statusBar().showMessage("✓ اجرا با موفقیت انجام شد")
            QMessageBox.information(self, "موفق", "فایل با موفقیت اجرا شد")
        else:
            self.statusBar().showMessage("✗ خطا در اجرا")
            if error:
                QMessageBox.critical(self, "خطا", f"خطا در اجرا:\n{error}")
    
    def stop_run(self):
        """Stop the current run"""
        if self.runner_thread and self.runner_thread.isRunning():
            self.runner_thread.terminate()
            self.running = False
            self.run_btn.setEnabled(True)
            self.stop_btn.setEnabled(False)
            self.progress_bar.setVisible(False)
            self.statusBar().showMessage("متوقف شد")
    
    def save_output(self):
        """Save the output to a file"""
        if not self.output_text.toPlainText():
            QMessageBox.warning(self, "خطا", "خروجی خالی است")
            return
        
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "ذخیره خروجی",
            "",
            "Text Files (*.txt);;All Files (*)"
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(self.output_text.toPlainText())
                QMessageBox.information(self, "موفق", f"خروجی ذخیره شد:\n{file_path}")
            except Exception as e:
                QMessageBox.critical(self, "خطا", f"خطا در ذخیره:\n{str(e)}")
    
    def load_recent_files(self):
        """Load and display recent files"""
        self.recent_list.clear()
        for file_path in config.recent_files:
            if os.path.isfile(file_path):
                item = QListWidgetItem(Path(file_path).name)
                item.setData(Qt.ItemDataRole.UserRole, file_path)
                self.recent_list.addItem(item)
    
    def on_recent_file_clicked(self, item: QListWidgetItem):
        """Handle recent file clicked"""
        file_path = item.data(Qt.ItemDataRole.UserRole)
        self.set_file(file_path)
    
    def open_recent_file(self):
        """Open the selected recent file"""
        current_item = self.recent_list.currentItem()
        if current_item:
            self.on_recent_file_clicked(current_item)
    
    def clear_recent_files(self):
        """Clear recent files list"""
        reply = QMessageBox.question(
            self,
            "تأیید",
            "آیا مطمئن هستید که می‌خواهید فایل های اخیر را پاک کنید؟"
        )
        if reply == QMessageBox.StandardButton.Yes:
            config.recent_files = []
            config.save_recent_files()
            self.load_recent_files()
    
    def toggle_theme(self):
        """Toggle between light and dark theme"""
        current_theme = config.get('theme', 'dark')
        new_theme = 'light' if current_theme == 'dark' else 'dark'
        config.set('theme', new_theme)
        self.apply_theme()
    
    def apply_theme(self):
        """Apply the current theme"""
        theme = config.get('theme', 'dark')
        if theme == 'dark':
            self.setStyleSheet(DARK_STYLESHEET)
            self.theme_btn.setText("☀️ روشن")
        else:
            self.setStyleSheet(LIGHT_STYLESHEET)
            self.theme_btn.setText("🌙 تیره")
    
    def open_settings(self):
        """Open settings dialog"""
        from ui.settings_dialog import SettingsDialog
        dialog = SettingsDialog(self)
        if dialog.exec():
            # Reload runner with new settings
            opensees_path = config.get('opensees_path', config.DEFAULT_OPENSEES_PATH)
            self.runner = TCLRunner(opensees_path)
            self.statusBar().showMessage("تنظیمات ذخیره شد")
    
    @staticmethod
    def create_icon():
        """Create a simple icon for the application"""
        pixmap = QPixmap(64, 64)
        pixmap.fill(QColor(14, 165, 233))
        return QIcon(pixmap)
