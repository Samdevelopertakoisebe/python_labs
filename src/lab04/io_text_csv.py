from ...src.lib.text import *
from pathlib import Path
import csv
from typing import Iterable, Sequence

def ensure_parent_dir(path: str | Path) -> None:
    """Для write_csv; создаёт все директории, которых не хватает до файла."""
    end_path = str(path).replace('\\', '/').rfind('/')
    Path(str(path)[:end_path]).mkdir(parents=True, exist_ok=True)


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает текст из данного пути, выводя его в одну строку.
    Возможен выбор другой кодировки через encoding=<...>"""
    p = Path(path)
    return normalize(p.read_text(encoding=encoding))


def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    """Записывает данные в .csv файл по указанному пути."""
    ensure_parent_dir(path)
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

#
# project_root = 'C:/Users/sambu/PycharmProjects/PythonProject7/python_labs/'
# use_path = project_root + 'data/lab04/diggers.csv'
# write_csv(['ла',['бу','бу']], use_path, ('бубу','бобо'))
# print(read_text(use_path, encoding="utf-8"))
# use_path = __file__[:__file__.rfind('\\')] + '\\test.csv'
# write_csv([('мяу','мяу'),'мяу'], use_path, ('мира','кот'))
# print(read_text(use_path, encoding="utf-8"))