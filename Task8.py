"""Створення директорії"""

from pathlib import Path

new_dir = Path('tmp')

if not new_dir.exists():
    new_dir.mkdir()

new_dir.mkdir(exist_ok=True)
