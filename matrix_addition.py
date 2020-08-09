X = [[1, 3], [2, 4]]
Y = [[5, 2], [1, 0]]
result = [[0, 0], [0, 0]]

for i in range(len(X)):
    for j in range(len(Y)):
        result[i][j] = X[i][j] + Y[i][j]

print(result)
