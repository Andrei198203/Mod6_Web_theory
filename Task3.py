"""Читаємо кілька файлів поспіль. Імена файлів для читання передаємо як аргументи командного рядка"""
import sys

if len(sys.argv) == 1:
    print("Set the file names as parameters in terminal")
    quit()

print(sys.argv)
for i in range(1, len(sys.argv)):
    file_name = sys.argv[i]
    print(file_name)
    try:
        with open(file_name, 'r', encoding="utf-8") as file:
            for line in file:
                print(line)
    except OSError:
        print(f"Error with right for file {file_name}")
