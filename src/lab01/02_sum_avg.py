a, b = float(input('a: ').replace(',', '.')), float(input('b: ').replace(',', '.'))
print('sum=' + str(round(a + b, 2)), end='; ')
print('avg=' + str(round((a + b) / 2, 2)))