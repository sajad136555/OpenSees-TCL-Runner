# -*- coding: utf-8 -*-
"""
Configuration management for OpenSees TCL Runner
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Any

class Config:
    """Configuration manager"""
    
    DEFAULT_OPENSEES_PATH = r"C:\ActiveTcl\bin\OpenSees.exe"
    DEFAULT_INITIAL_DIR = "H:\\"
    
    def __init__(self):
        self.config_dir = Path.home() / ".opensees_runner"
        self.config_file = self.config_dir / "config.json"
        self.recent_files_file = self.config_dir / "recent_files.json"
        
        # Create config directory if it doesn't exist
        self.config_dir.mkdir(exist_ok=True)
        
        self.config = self._load_config()
        self.recent_files = self._load_recent_files()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading config: {e}")
        
        return {
            'opensees_path': self.DEFAULT_OPENSEES_PATH,
            'initial_dir': self.DEFAULT_INITIAL_DIR,
            'theme': 'dark',
            'window_size': [1200, 800],
            'auto_save': True,
            'font_size': 12,
        }
    
    def _load_recent_files(self) -> List[str]:
        """Load recent files list"""
        if self.recent_files_file.exists():
            try:
                with open(self.recent_files_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return data.get('files', [])
            except Exception as e:
                print(f"Error loading recent files: {e}")
        
        return []
    
    def save_config(self):
        """Save configuration to file"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving config: {e}")
    
    def save_recent_files(self):
        """Save recent files list"""
        try:
            with open(self.recent_files_file, 'w', encoding='utf-8') as f:
                json.dump({'files': self.recent_files}, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving recent files: {e}")
    
    def add_recent_file(self, file_path: str):
        """Add file to recent files list"""
        if file_path in self.recent_files:
            self.recent_files.remove(file_path)
        
        self.recent_files.insert(0, file_path)
        
        # Keep only last 10 files
        self.recent_files = self.recent_files[:10]
        self.save_recent_files()
    
    def get(self, key: str, default=None):
        """Get configuration value"""
        return self.config.get(key, default)
    
    def set(self, key: str, value):
        """Set configuration value"""
        self.config[key] = value
        self.save_config()

# Global config instance
config = Config()
