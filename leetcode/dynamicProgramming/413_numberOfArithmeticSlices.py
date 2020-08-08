import unittest
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        dp = [0] * len(A)
        sum = 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp[i] += 1 + dp[i - 1]
                sum += dp[i]
        return sum


class Test(unittest.TestCase):
    def test_one(self):
        nums = [1, 2, 3, 4]
        answer = 3

        result = Solution().numberOfArithmeticSlices(nums)
        self.assertEqual(answer, result)
