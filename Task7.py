"""Видалення файлу"""

from pathlib import Path

try:
    tmp = Path('jokes.txt')
    tmp.unlink()
except FileNotFoundError:
    pass