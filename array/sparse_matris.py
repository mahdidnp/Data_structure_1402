def sparseMatrix(sparce, n):
    arr = []
    size = 0
    arr.append([n, n, 0])
    for i in range(n):
        for j in range(n):
            if sparce[i][j] != 0:
                arr.append([i, j, sparce[i][j]])
                size = size + 1
    
    arr[0][2] = size
    return arr


# Test:
compactMatrix = sparseMatrix([
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 1],
], 3)

for i in range(len(compactMatrix)):
    print(compactMatrix[i])