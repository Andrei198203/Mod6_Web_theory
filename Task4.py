"""Читаємо файл за допомогою бібліотеки pathlib
Без оператора with. Необхідно закрити файл самому"""

from pathlib import Path

file_name = Path('./Temp')

try:
    file = open(file_name / 'jokes.txt', 'r', encoding='utf-8')
    try:
        while True:
            line = file.readline()
            if not line:
                break
            print(line, end="")
    except OSError:
        print("Error while reading file")
    finally:
        file.close()
except OSError:
    print("OSError")