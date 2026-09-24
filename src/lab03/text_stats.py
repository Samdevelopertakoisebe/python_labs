from sys import stdin
from python_labs.src.lib.text import *

text = stdin.read()
text = tokenize(normalize(text))
print('Всего слов:', len(text))
text = count_freq(text)
print('Уникальных слов:', len(text))

USE_TABLE = True

if USE_TABLE:
    col_len = max(text.values()) + 5
    text = top_n(text, n=5)
    print('слово' + ' ' * (col_len - 5) + '| частота')
    print('-' * (col_len + 9))
    for i in text:
        print(i[0] + ' ' * (col_len - len(i[0])) + '|', i[1])

else:
    print('Топ-5:')
    for i in text.keys():
        print(f'{i}: {text[i]}')