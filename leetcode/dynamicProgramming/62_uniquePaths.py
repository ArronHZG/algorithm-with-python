import unittest
from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


class Test(unittest.TestCase):
    def test_one(self):
        m = 3  # 列
        n = 2  # 行
        answer = 3

        result = Solution().uniquePaths(m, n)
        self.assertEqual(answer, result)
