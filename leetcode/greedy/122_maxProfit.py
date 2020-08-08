import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            profit += max(prices[i] - prices[i - 1], 0)

        return profit


class Test(unittest.TestCase):
    def test_one(self):
        nums = [7, 1, 5, 3, 6, 4]
        answer = 7

        result = Solution().maxProfit(nums)
        self.assertEqual(answer, result)
