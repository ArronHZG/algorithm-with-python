import unittest
from typing import List


class Solution:
    def __init__(self):
        self.dp = []
        for i in range(5):
            self.dp.append(i)

    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1
        elif 4 < n < len(self.dp):
            return self.dp[n]

        for i in range(len(self.dp), n + 1):
            max_i = 0
            for j in range(2, i // 2 + 1):
                max_i = max(self.dp[j] * self.dp[i - j], max_i)
            self.dp.append(max_i)

        return self.dp[n]


class Test(unittest.TestCase):
    def test_one(self):
        nums = 10
        answer = 36

        result = Solution().integerBreak(nums)
        self.assertEqual(answer, result)
