import unittest
from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if not grid or grid[0][0] == 1 or grid[- 1][- 1] == 1:
            return -1
        path = deque()
        path.append([0, 0])
        grid[0][0] = 1
        while path:
            first_x, first_y = path.popleft()
            for i in range(-1, 2):
                for j in range(-1, 2):
                    x = first_x + i
                    y = first_y + j
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                        grid[x][y] = grid[first_x][first_y] + 1
                        path.append([x, y])

        return grid[- 1][- 1] if grid[- 1][- 1] != 0 else -1


class MyTestCase(unittest.TestCase):
    def test_something(self):
        nums = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
        answer = 4
        result = Solution().shortestPathBinaryMatrix(nums)
        self.assertEqual(answer, result)
