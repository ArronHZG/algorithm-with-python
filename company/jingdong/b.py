def show(grid):
    for i in grid:
        print(i)
    print()


def findWay(grid, n, m, start):
    flag = [False]

    def dfs(x, y):
        if 0 <= x < n and 0 <= y < m:
            if grid[x][y] == 'E':
                flag[0] = True
                return
            if grid[x][y] == '.':
                grid[x][y] = '#'
                if not flag[0]:
                    dfs(x - 1, y)
                if not flag[0]: 
                    dfs(x, y - 1)
                if not flag[0]:
                    dfs(x + 1, y)
                if not flag[0]:
                    dfs(x, y + 1)

    grid[start[0]][start[1]] = '.'
    dfs(start[0], start[1])

    if flag[0]:
        print('YES')
    else:
        print('NO')


T = int(input())
for _ in range(T):
    line = [int(x) for x in input().split()]
    n, m = line[0], line[1]
    start = [-1, -1]
    grid = []
    for i in range(n):
        line = input()
        grid.append(list(line))
        for j, c in enumerate(line):
            if c == 'S':
                start = [i, j]
    findWay(grid, n, m, start)
