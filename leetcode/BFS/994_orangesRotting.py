import collections
import unittest
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        R, C = len(grid), len(grid[0])

        # queue - all starting cells with rotting oranges
        queue = collections.deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c, 0))

        def neighbors(r, c):
            for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        d = 0
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d + 1))

        if any(1 in row for row in grid):
            return -1
        return d


class Test(unittest.TestCase):
    def test_one(self):
        nums = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        answer = 4

        result = Solution().orangesRotting(nums)
        self.assertEqual(answer, result)


if __name__ == '__main__':
    unittest.main()
