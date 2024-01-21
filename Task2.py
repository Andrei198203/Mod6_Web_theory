"""Прочитати кінець файлу, останні N рядків файлу.
Ім'я файлу для читання передаємо як аргумент командного рядка"""


import sys

NUM_LINES = 10

if len(sys.argv) != 2:
    print("Not enough parameters")
    quit()

try:
    with open(sys.argv[1], 'r', encoding="utf-8") as file:
        lines = list()
        for line in file:
            lines.append(line)
            if len(lines) > NUM_LINES:
                lines.pop(0)
        for line in lines:
            print(line)
except OSError:
    print("Error with right for file")