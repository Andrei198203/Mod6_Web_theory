"""За допомогою оператора with. Менше коду та зручність"""

from pathlib import Path

file_name = Path('./Temp')

try:
    with open(file_name / 'jokes.txt', 'r', encoding='utf-8') as file:
        # print(file.readlines())
        for line in file:
            print(line, end="")
except OSError:
    print("Error while reading file")