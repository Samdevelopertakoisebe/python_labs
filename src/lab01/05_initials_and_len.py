a = input('ФИО: ').strip().split()
print('Инициалы:', ''.join([i[0]for i in a]) + '.')
print('Длина (символов):', sum(map(len, a)) + len(a) - 1)