import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        sell = prices[-1]
        money = 0
        for i in range(len(prices) - 2, -1, -1):
            if sell > prices[i]:
                money = max(money, sell - prices[i])
            else:
                sell = prices[i]
        return money


class Test(unittest.TestCase):
    def test_one(self):
        nums = [7, 1, 5, 3, 6, 4]
        answer = 5

        result = Solution().maxProfit(nums)
        self.assertEqual(answer, result)
