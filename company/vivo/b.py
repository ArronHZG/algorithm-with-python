import unittest
from collections import deque
from typing import List


def shortestPathBinaryMatrix(start, end, grid):
    n = len(grid)
    if not grid:
        return -1
    if grid[start[0]][start[1]] == '#' or grid[start[0]][start[1]] == '&':
        return -1
    grid_map = [[0] * n for _ in range(n)]
    path = deque()
    path.append(start)
    grid_map[start[0]][start[1]] = 1

    while path:
        print(grid_map)
        first_x, first_y = path.popleft()
        for i in range(-1, 2):
            for j in range(-1, 2):
                x = first_x + i
                y = first_y + j
                if 0 <= x < n and 0 <= y < n and grid_map[x][y] == 0 and (grid[x][y] != '#' or grid[x][y] != '&'):
                    grid_map[x][y] = grid_map[first_x][first_y] + 1
                    path.append([x, y])

    return grid_map[end[0]][end[1]] if grid_map[end[0]][end[1]] != 0 else -1


n = int(input())
line = [int(x) for x in input().split(' ')]

start = [line[0], line[1]]
end = [line[2], line[3]]

grid = []
for i in range(n):
    line = input()
    grid.append(list(line))

re = shortestPathBinaryMatrix(start, end, grid)

print(re)
