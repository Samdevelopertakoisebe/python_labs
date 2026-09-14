b = []
for i in range(int(input())):
    a = input().split()
    b.append([a[0], a[1], int(a[2]), a[3] == 'True'])
print(sum([1 for i in b if i[-1]]), sum([1 for i in b if not i[-1]]))

