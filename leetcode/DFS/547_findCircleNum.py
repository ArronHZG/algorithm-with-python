import unittest
from typing import List


class Solution:

    def findCircleNum(self, M: List[List[int]]) -> int:
        self.n, self.M = len(M), M
        res = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.M[i][j] == 1:
                    res += 1
                    self.dfs(i, j)

        return res

    def dfs(self, x, y):
        self.M[x][y] = 0
        print(self.M)
        for j in range(self.n):
            if self.M[y][j] == 1:
                self.dfs(y, j)


class Test(unittest.TestCase):
    def test_one(self):
        nums = [[1, 1, 0],
                [1, 1, 0],
                [0, 0, 1]]
        answer = 2
        result = Solution().findCircleNum(nums)
        self.assertEqual(answer, result)

    def test_two(self):
        nums = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
        answer = 1
        result = Solution().findCircleNum(nums)
        self.assertEqual(answer, result)
