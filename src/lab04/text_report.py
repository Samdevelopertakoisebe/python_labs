import argparse, sys

from ..lab03.text_stats import stats_wo_table, table
from .io_text_csv import *

def analyze(**kwargs) -> None:
    """Составляет отчёт о предоставленном, если тот отсутствует - поднимает FNFE.\n
    kwarg-и:\n
    \tsrc_file_paths: пути до файлов, по умолчанию ./data/input.txt\n
    \tout_file_path: путь до отчёта, по умолчанию ./data/report.txt\n
    \tencoding: кодировка, при случаях, когда кодировка читаемых файлов не utf-8"""
    src_file_paths = (Path(__file__[:-14] + 'data\\input.txt'),)
    out_file_path = Path(__file__[:-14] + 'data\\report.csv')
    enc = 'utf-8'
    if kwargs.get('src_file_paths') is not None: src_file_paths = kwargs.get('src_file_paths')
    if kwargs.get('out_file_path') is not None: out_file_path = kwargs.get('out_file_path')
    if kwargs.get('encoding') is not None: enc = kwargs.get('encoding')
    result = []
    for cur_file in src_file_paths:
        if not Path.exists(cur_file): raise FileNotFoundError(f"Файл {cur_file} не найден.")
        text = tokenize(normalize(read_text(cur_file, enc)))
        text = stats_wo_table(text)
        table(text)
        text = top_n(text, len(text))
        cur_file = str(cur_file)
        result.extend((cur_file[cur_file.rfind('\\') + 1:], text))
    if len(result) < 2:
        write_csv(result[1], out_file_path, ('words', 'count'))
        # TODO понять почему это чудо не работает
    else:
        # TODO
        pass


parser = argparse.ArgumentParser()
parser.add_argument("--in", dest="src_override")
parser.add_argument("--out", dest="out_override")
parser.add_argument("--encoding", dest="enc_override")
args = parser.parse_args()
# print(args.src_override)
# print(args.out_override)
# print(list(map(lambda x: Path(__file__[:-14] + x), args.src_override.split(','))))
analyze()
# analyze(list(map(lambda x: Path(__file__[:-14] + x), args.src_override.split(','))),
#         Path(__file__[:-14] + args.out_override),
#         encoding=args.enc_override)

