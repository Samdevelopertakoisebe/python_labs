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
    return sorted([(i, freq[i]) for i in freq.keys()], key=lambda x: (2**63-x[1], x[0]))[:n]

# a = ["a","b","a","c","b","a"]
# print(a := count_freq(a))
# print(top_n(a, n=2))
# print()
# a = ["bb","aa","bb","aa","cc"]
# print(a := count_freq(a))
# print(top_n(a, n=2))


# # normalize
# assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
# assert normalize("ёжик, Ёлка") == "ежик, елка"
#
# # tokenize
# assert tokenize("привет, мир!") == ["привет", "мир"]
# assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
# assert tokenize("2025 год") == ["2025", "год"]
#
# # count_freq + top_n
# freq = count_freq(["a","b","a","c","b","a"])
# assert freq == {"a":3, "b":2, "c":1}
# assert top_n(freq, 2) == [("a",3), ("b",2)]
#
# # тай-брейк по слову при равной частоте
# freq2 = count_freq(["bb","aa","bb","aa","cc"])
# assert top_n(freq2, 2) == [("aa",2), ("bb",2)]