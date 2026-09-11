# -*- coding: utf-8 -*-
"""
TCL file runner for OpenSees
"""

import subprocess
import os
from pathlib import Path
from typing import Tuple, Optional
from datetime import datetime

class TCLRunner:
    """Runner for executing TCL files with OpenSees"""
    
    def __init__(self, opensees_path: str):
        """
        Initialize the runner
        
        Args:
            opensees_path: Path to OpenSees executable
        """
        self.opensees_path = opensees_path
        self.last_output = ""
        self.last_error = ""
    
    def is_opensees_available(self) -> bool:
        """Check if OpenSees is available"""
        return os.path.isfile(self.opensees_path)
    
    def run_file(self, file_path: str) -> Tuple[bool, str, str]:
        """
        Run a TCL file with OpenSees
        
        Args:
            file_path: Path to TCL file
        
        Returns:
            Tuple of (success, output, error)
        """
        if not os.path.isfile(file_path):
            error_msg = f"فایل یافت نشد: {file_path}"
            self.last_error = error_msg
            return False, "", error_msg
        
        try:
            # Log execution
            log_msg = f"\n{'='*60}\n"
            log_msg += f"اجرای شد: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            log_msg += f"فایل: {file_path}\n"
            log_msg += f"{'='*60}\n\n"
            
            # Run the file
            result = subprocess.run(
                [self.opensees_path, file_path],
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )
            
            self.last_output = log_msg + result.stdout
            self.last_error = result.stderr
            
            success = result.returncode == 0
            
            if success:
                self.last_output += f"\n{'='*60}\n✓ اجرا با موفقیت انجام شد\n"
            else:
                self.last_output += f"\n{'='*60}\n✗ کد خ��وج: {result.returncode}\n"
            
            return success, self.last_output, self.last_error
        
        except subprocess.TimeoutExpired:
            error_msg = "خطا: زمان اجرا بیش از حد مجاز است (5 دقیقه)"
            self.last_error = error_msg
            return False, self.last_output, error_msg
        
        except Exception as e:
            error_msg = f"خطا در اجرا: {str(e)}"
            self.last_error = error_msg
            return False, self.last_output, error_msg
    
    def get_file_info(self, file_path: str) -> dict:
        """Get information about a TCL file"""
        if not os.path.isfile(file_path):
            return {}
        
        file = Path(file_path)
        stat = file.stat()
        
        return {
            'name': file.name,
            'path': file_path,
            'size': stat.st_size,
            'size_human': self._human_readable_size(stat.st_size),
            'modified': datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
            'lines': self._count_lines(file_path)
        }
    
    @staticmethod
    def _human_readable_size(size: int) -> str:
        """Convert bytes to human readable format"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.2f} {unit}"
            size /= 1024.0
        return f"{size:.2f} TB"
    
    @staticmethod
    def _count_lines(file_path: str) -> int:
        """Count lines in a file"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return len(f.readlines())
        except:
            return 0
