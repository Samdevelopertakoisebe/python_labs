from python_labs.src.lib.text import *
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает текст из данного пути, выводя его в одну строку.
    Возможен выбор другой кодировки через encoding=<...>"""
    p = Path(path)
    return p.read_text(encoding=encoding)


path = 'C:/Users/sambu/PycharmProjects/PythonProject7/python_labs/' + 'data/lab04/text.txt'
print(a)
assert read_text(path) == 'fsina'