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

print(transpose([[4, 1, 5]]))
print(transpose([[5], [10], [1]]))
print(transpose([]))
print(transpose([[11, 12], [9, 10]]))
print(transpose([[1111], [1, 2, 3]]))

print()
def row_sums(mat: list[list[float | int]]) -> list[float]:
    if any(len(mat[0]) != len(mat[i]) for i in range(len(mat))):
        return 'ValueError'
    
    elif len(mat) == 0:
        return []
    
    summa = []
    for arr in range(len(mat)):
        summa.append(sum(mat[arr]))
    return summa

print(row_sums([[100, 1, 12], [1, 2, 3]]))
print(row_sums([[-10, 0], [-9, 1]]))
print(row_sums([[0, 0, 0], [0, 0, 0]]))
print(row_sums([[1, 2], [3]]))

print()
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

print(col_sums([[2, 3, 6], [1, 4, 5]]))
print(col_sums([[-1000, 10], [-1, -4]]))
print(col_sums([[0], [0]]))
print(col_sums([[1], [5, 8, 0]]))