def printAllPathsUtil(mat, i, j, m, n, path, pi):
    if (i==m-1):
        for k in range(j, n):
            path[pi + k-j] = mat[i][k]
        for l in range(pi + n -j):
            print(path[l], end =" ")
        print()
        return

    if (j == n-1):
        for k in range(i, m):
            path[pi + k-i] = mat[k][j]
        for l in range(pi + m-i):
            print(path[l], end=" ")
        print()
        return
    path[pi] = mat[i][j]
    printAllPathsUtil(mat, i + 1, j, m, n, path, pi + 1)
    printAllPathsUtil(mat, i, j + 1, m, n, path, pi + 1)

def printAllPaths(mat, m, n):
    path = [0 for i in range(m + n)]
    printAllPathsUtil(mat, 0, 0, m, n, path, 0)

mat = [[1, 2, 3],
        [4, 5, 6]]
printAllPaths(mat, 2, 3)

# This code is contributed by Mohit Kumar

