b = []
for i in range(int(input('Кол-во студентов: '))):
    a = input(f'Данные {i + 1}-го студента: ').split()
    b.append([a[0], a[1], int(a[2]), a[3] == 'True'])
print(sum([1 for i in b if i[-1]]), sum([1 for i in b if not i[-1]]))

