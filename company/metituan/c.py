from collections import deque


def fun(n, x, y, grid):
    print(grid)

    dq = deque()
    dq.appendleft(y)
    for i in range(n):
        if grid[i][y] == 1:
            grid[i][y] += 1

    while dq:
        tmp = dq.pop()
        for i in range(n):
            if grid[tmp][i] == 1:
                grid[tmp][i] += 1
                dq.appendleft(i)
        print(grid)
        print(dq)


# line = [int(x) for x in input().strip().split(' ')]
# n = line[0]
# x = line[1]
# y = line[2]
# grid = [[0] * (n + 1) for i in range(n + 1)]
# for i in range(n - 1):
#     arr = [int(x) for x in input().strip().split(' ')]
#     grid[arr[0]][arr[1]] = 1
#     grid[arr[1]][arr[0]] = 1

grid = [[0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0]]
n = 6
x = 1
y = 2
fun(n, x, y, grid)
