def normalize(text: str, casefold: bool = True, yo2e:bool = True) -> str:
    if casefold: text = text.casefold()
    if yo2e: text = text.replace('ё', 'е').replace('Ё', 'Е')
    text = text.replace('\n', ' ')
    text = text.replace('\r', ' ')
    text = text.replace('\t', ' ')
    return ' '.join([i for i in text.strip().split() if i != ''])

# print(normalize("ПрИвЕт\nМИр\t"))
# print(normalize("ёжик, Ёлка"))
# print(normalize("Hello\r\nWorld"))
# print(normalize("  двойные   пробелы  "))

import string


def tokenize(text: str) -> list[str]:
    res = []
    cur = ''
    russian = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    incl = russian + russian.lower() + string.ascii_letters + string.digits + '_-'
    for i in text:
        if i in incl:
            cur += i
        elif cur != '':
            res.append(cur)
            cur = ''
    return res + ([cur] if cur != '' else [])

# print(tokenize("привет мир"))
# print(tokenize("hello,world!!!"))
# print(tokenize("по-настоящему круто"))
# print(tokenize("2025 год"))
# print(tokenize("emoji 😀 не слово"))

def count_freq(tokens: list[str]) -> dict[str, int]:
    res = dict.fromkeys(tokens, 0)
    for token in tokens:
        res[token] += 1
    return res

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    return sorted([(i, freq[i]) for i in freq.keys()], key=lambda x: (x[1], x[0]))[:n]

# a = ["a","b","a","c","b","a"]
# print(a := count_freq(a))
# print(top_n(a, n=2))
# print()
# a = ["bb","aa","bb","aa","cc"]
# print(a := count_freq(a))
# print(top_n(a, n=2))
