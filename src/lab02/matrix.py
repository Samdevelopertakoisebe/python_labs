def transpose(mat):
    if any([len(mat[i]) != len(mat[i + 1]) for i in range(len(mat) - 1)]):
        raise ValueError('Ne matriza')
    res = []
    if len(mat) > 0:
        for i in range(len(mat[0])):
            res.append([mat[j][i] for j in range(len(mat))])
    return res

# print(transpose([[1, 2, 3]]))
# print(transpose([[1], [2], [3]]))
# print(transpose([[1, 2], [3, 4]]))
# print(transpose([]))
# print(transpose([[1, 2], [3]]))

def row_sums(mat):
    if any([len(mat[i]) != len(mat[i + 1]) for i in range(len(mat) - 1)]):
        raise ValueError('Ne matriza')
    return [sum(i) for i in mat]

# print(row_sums([[1, 2, 3], [4, 5, 6]]))
# print(row_sums([[-1, 1], [10, -10]]))
# print(row_sums([[0, 0], [0, 0]]))
# print(row_sums([[1, 2], [3]]))

def col_sums(mat):
    if any([len(mat[i]) != len(mat[i + 1]) for i in range(len(mat) - 1)]):
        raise ValueError('Ne matriza')
    return [sum([mat[j][i] for j in range(len(mat))]) for i in range(len(mat[0]))]

print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))