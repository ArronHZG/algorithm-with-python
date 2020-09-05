import unittest
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            if 0 <= x < n and 0 <= y < m and grid[x][y] == '1':
                grid[x][y] = '0'
                for i, j in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                    dfs(x + i, y + j)

        nums = 0
        if grid:
            n, m, grid = len(grid), len(grid[0]), grid
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == '1':
                        nums += 1
                        dfs(i, j)
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
