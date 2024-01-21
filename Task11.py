"""Робота з різними кодуваннями"""

from pathlib import Path

message = "Hello, Привіт"

print(message.encode())
print(message.encode("utf_16"))
print(message.encode("cp1251"))
print(b'\xff\xfeH\x00e\x00l\x00l\x00o\x00,\x00 \x00\x1f\x04@\x048\x042\x04V\x04B\x04'.decode('cp1251'))

folder = Path("Temp")

with open(folder/"utf_8.txt", "wb") as f:
    f.write(message.encode())

with open(folder/"utf_16.txt", "wb") as f:
    f.write(message.encode("utf-16"))

with open(folder/"cp1251.txt", "wb") as f:
    f.write(message.encode("cp1251"))

with open(folder/"cp1251.txt", "rb") as f:
    print(f.read().decode("cp1251"))

with open(folder/"utf_8.txt", "rb") as f:
    print(f.read().decode("utf-8"))