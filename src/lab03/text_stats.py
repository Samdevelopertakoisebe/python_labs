from sys import stdin
from ...src.lib.text import *

def stats_wo_table(tknzd_txt):
    print('Всего слов:', len(tknzd_txt))
    tknzd_txt = count_freq(tknzd_txt)
    print('Уникальных слов:', len(tknzd_txt))
    return tknzd_txt

def table(freq_text):
    col_len = max(freq_text.values()) + 5
    freq_text = top_n(freq_text, n=5)
    print('слово' + ' ' * (col_len - 5) + '| частота')
    print('-' * (col_len + 9))
    for i in freq_text:
        print(i[0] + ' ' * (col_len - len(i[0])) + '|', i[1])


if __name__ == "__main__":
    text = stdin.read()
    text = tokenize(normalize(text))
    if len(text) == 0:
        print('Нету текста для статистики.')
        quit()
    text = stats_wo_table(text)

    USE_TABLE = True

    if USE_TABLE:
        table(text)

    else:
        print('Топ-5:')
        for i in text.keys():
            print(f'{i}: {text[i]}')