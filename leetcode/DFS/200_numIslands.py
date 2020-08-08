import unittest
from typing import List


class Solution:

    def __init__(self):
        self.n, self.m, self.grid = 0, 0, 0

    def dfs(self, x, y):
        if 0 <= x < self.n and 0 <= y < self.m and self.grid[x][y] == '1':
            self.grid[x][y] = '0'
            for i, j in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                self.dfs(x + i, y + j)

    def numIslands(self, grid: List[List[str]]) -> int:
        nums = 0
        if grid:
            self.n, self.m, self.grid = len(grid), len(grid[0]), grid
            for i in range(self.n):
                for j in range(self.m):
                    if grid[i][j] == '1':
                        nums += 1
                        self.dfs(i, j)
        return nums


class Test(unittest.TestCase):
    def test_one(self):
        nums = [['0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0'],
                ['0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0'],
                ['0', '1', '0', '0', '1', '1', '0', '0', '1', '0', '1', '0', '0'],
                ['0', '1', '0', '0', '1', '1', '0', '0', '1', '1', '1', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0']]

        answer = 6

        result = Solution().numIslands(nums)
        self.assertEqual(answer, result)
