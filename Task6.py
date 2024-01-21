"""Використання glob"""

from pathlib import Path
list_dir = Path('.')

for elem in list_dir.glob('*.py'):
    print(elem)