import math
import unittest
from typing import List


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                else:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        return int(dp[-1]) if dp[-1] != amount + 1 else -1


class Test(unittest.TestCase):
    def test_one(self):
        coins = [1, 2, 5]
        amount = 11
        answer = 3
        result = Solution().coinChange(coins, amount)
        self.assertEqual(answer, result)

    def test_two(self):
        coins = [2]
        amount = 3
        answer = -1
        result = Solution().coinChange(coins, amount)
        self.assertEqual(answer, result)
