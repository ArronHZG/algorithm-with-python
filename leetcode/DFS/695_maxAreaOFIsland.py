import unittest
from typing import List


class Solution:

    def __init__(self):
        self.n, self.m, self.grid = 0, 0, 0

    def dfs(self, x, y):
        island = 0
        if 0 <= x < self.n and 0 <= y < self.m and self.grid[x][y] == 1:
            self.grid[x][y] = 0
            island = 1
            for i, j in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                island += self.dfs(x + i, y + j)
        return island

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.n, self.m, self.grid = len(grid), len(grid[0]), grid
        max_area = 0
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 1:
                    max_area = max(self.dfs(i, j), max_area)
        return max_area


class Test(unittest.TestCase):
    def test_one(self):
        nums = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

        answer = 6

        result = Solution().maxAreaOfIsland(nums)
        self.assertEqual(answer, result)
