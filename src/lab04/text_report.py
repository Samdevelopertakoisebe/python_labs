from io import StringIO
import argparse
from python_labs.src.lib.text import *
from python_labs.src.lab04.io_text_csv import *
import sys

path = 'data/lab04/diggers.csv'
parser = argparse.ArgumentParser()
parser.add_argument("--in", dest="input_file")
parser.add_argument("--out", dest="input_file")
args = parser.parse_args()

print(args.input_file)


root_path = 'C:/Users/sambu/PycharmProjects/PythonProject7/python_labs/'
path = root_path + path

text = read_text(path)
sys.stdin = StringIO(text)

from python_labs.src.lab03 import text_stats

text = count_freq(tokenize(normalize(text)))
text_len = len(text)
res = top_n(text, text_len)
write_csv(res, path, ('words', 'count'))


