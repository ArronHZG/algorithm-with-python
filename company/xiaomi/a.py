line = [int(x) for x in input().split()]
n = line[0]
m = line[1]
grid = []
for i in range(n):
    line = [int(x) for x in input().split()]
    grid.append(line)


def fun(grid, n, m):
    def go(i, j):
        tmp[0] += grid[i][j]
        if i == n - 1 and j == m - 1:
            res.append(tmp[0])
        if i + 1 < n:
            go(i + 1, j)
        if j + 1 < m:
            go(i, j + 1)
        tmp[0] -= grid[i][j]

    tmp = [0]
    res = []

    go(0, 0)

    print(max(res))


fun(grid, n, m)
