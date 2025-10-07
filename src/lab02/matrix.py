def transpose(mat: list[list[float | int]]) -> list[list]:    
    if any(len(mat[0]) != len(mat[i]) for i in range(len(mat))):
        return 'ValueError'
    
    elif len(mat) == 0:
        return []
            
    new_matrix = [[0 for i in range(len(mat))] for x in range(len(mat[0]))]
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            new_matrix[y][x] = mat[x][y]
    return new_matrix

print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))


def row_sums(mat: list[list[float | int]]) -> list[float]:
    if any(len(mat[0]) != len(mat[i]) for i in range(len(mat))):
        return 'ValueError'
    
    elif len(mat) == 0:
        return []
    
    summa = []
    for arr in range(len(mat)):
        summa.append(sum(mat[arr]))
    return summa

print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if any(len(mat[0]) != len(mat[i]) for i in range(len(mat))):
        return 'ValueError'
    
    elif len(mat) == 0:
        return []
    
    summa = [0 for i in range(len(mat[0]))]
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            summa[y] += (mat[x][y])
    return summa

print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))


        