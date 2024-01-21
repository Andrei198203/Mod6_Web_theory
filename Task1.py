"""Задачі для теоретичного заняття шостого дня
Задачі теоретичного блоку: продемонструвати на практичному прикладі теорію повязану з читанням файлів,
записом даних у менеджером контексту видами кодування, робота з нетекстовими файлами і архівами."""

"""Прочитати перші N рядків текстового файлу. Імя файлу для читання передаємо як аргумент командного рядка"""

import sys

NUM_LINES = 10

if len(sys.argv) != 2:
    print("Not enough parameters")
    quit()

try:
    file = open(sys.argv[1], "r", encoding="utf-8")
    try:
        line = file.readline()
        count = 0
        while count < NUM_LINES and line != "":
            line = line.rstrip()
            print(line)
            count += 1
            line = file.readline()
    except OSError:
        print("Error while reading file")
    finally:
        file.close()
except OSError:
    print("Error with right for file")

