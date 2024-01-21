"""Робота з файлами засобами pathlib"""

# from pathlib import Path
#
# message = Path('test_file.txt')
#
# message.write_text("First line")
# message.write_text("Second line")
# message.write_text("First line\nFinal line")
#
# print(message.read_text())

"""Бінарний файл"""

from pathlib import Path

message = Path('test_binary.txt')
message.write_bytes(b"Second line 123")
print(message.read_bytes().decode())
