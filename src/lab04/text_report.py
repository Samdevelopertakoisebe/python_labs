import argparse

from ..lab03.text_stats import stats_wo_table, table
from .io_text_csv import *

def analyze(arguments=None) -> None:
    """Составляет отчёт о предоставленном, если тот отсутствует - поднимает FileNotFoundError.
    При подаче разделяет траекторию до файла на 2 для хранения индивидуальных и общих отсчётов.\n
    arg-и: (<Any>, str)\n
    \tsrc_file_paths: пути до файлов, по умолчанию ./data/input.txt\n
    \tout_file_path: путь до отчёта, по умолчанию ./data/report.txt\n
    \tencoding: кодировка, при случаях, когда кодировка читаемых файлов не utf-8"""
    if arguments is None:
        arguments = {}
    src_file_paths = (Path(__file__[:-14] + 'data\\input.txt'),)
    out_file_path = Path(__file__[:-14] + 'data\\report.csv')
    enc = 'utf-8'
    if 'srcs' in arguments.keys(): src_file_paths = arguments['srcs']
    if 'out' in arguments.keys(): out_file_path = arguments['out']
    if 'enc' in arguments.keys(): enc = arguments['enc']
    result = []
    for cur_file in src_file_paths:
        print()
        print(cur_file)
        if not Path.exists(cur_file):
            raise FileNotFoundError(f"Файл {cur_file} не найден.")
        text = tokenize(normalize(read_text(cur_file, enc)))
        text = stats_wo_table(text)
        table(text)
        text = top_n(text, len(text))
        cur_file = str(cur_file)
        result.append((cur_file[cur_file.rfind('\\') + 1:], text))
    result.sort(key=lambda x: x[0])
    if len(result) < 2:
        write_csv((result[0][1] if len(result) == 1 else []), out_file_path, ('words', 'count'))
    else:
        result_plus = []
        for i in result:
            result_plus.extend([(i[0], j[0], j[1]) for j in i[1]])
        out_file_individual = out_file_path.with_name(f"{out_file_path.stem}_individual{out_file_path.suffix}")
        write_csv(result_plus, out_file_individual, ('file', 'words', 'count'))
        result_plus_ultra= {}
        for i in result_plus:
            if i[1] not in result_plus_ultra: result_plus_ultra[i[1]] = i[2]
            else: result_plus_ultra[i[1]] += i[2]
        result_plus_ultra = sorted([(i, result_plus_ultra[i]) for i in result_plus_ultra], key=lambda x: [-x[1], x[0]])
        out_file_total = out_file_path.with_name(f"{out_file_path.stem}_total{out_file_path.suffix}")
        write_csv(result_plus_ultra, out_file_total, ('words', 'count'))


parser = argparse.ArgumentParser()
parser.add_argument("--in", dest="src_override")
parser.add_argument("--out", dest="out_override")
parser.add_argument("--encoding", dest="enc_override")
args = parser.parse_args()
# print(args.src_override)
# print(args.out_override)
# print(list(map(lambda x: Path(__file__[:-14] + x), args.src_override.split(','))))
active_args = {}
if args.src_override is not None: active_args['srcs'] = list(map(lambda x: Path(__file__[:-14] + x),
                                                                 args.src_override.split(',')))
if args.out_override is not None: active_args['out'] = Path(__file__[:-14] + args.out_override)
if args.enc_override is not None: active_args['enc'] = args.enc_override
analyze(active_args)

