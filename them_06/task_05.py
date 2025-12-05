def matrix_intersection(a, b):
    res = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[i])):
            if a[i][j] != b[i][j]:
                row.append(-1)
            else:
                row.append(a[i][j])
        res.append(row)

    return res


a = [[1, 2], [3, 4]]
b = [[2, 2], [4, 4]]
print(matrix_intersection(a, b))
# [[-1, 2], [-1, 4]]


a = [[3, 2, 1], [4, 2, 2], [3, 1, 2]]
b = [[3, 4, 5], [6, 2, 7], [7, 8, 2]]
print(matrix_intersection(a, b))
# [[3, -1, -1], [-1, 2, -1], [-1, -1, 2]]
