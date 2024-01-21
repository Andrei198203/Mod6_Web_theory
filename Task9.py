"""Створення вкладених директорій"""

from pathlib import Path

new_dir = Path('Test/tmp/tests/tmps')

print(new_dir)
new_dir.mkdir(parents=True, exist_ok=True)