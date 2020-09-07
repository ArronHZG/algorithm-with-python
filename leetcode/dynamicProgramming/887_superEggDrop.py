import unittest
from functools import lru_cache
from typing import List


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        @lru_cache(None)
        def calcF(k, t):
            if t == 1 or k == 1:
                return t + 1
            return calcF(k - 1, t - 1) + calcF(k, t - 1)

        T = 1
        while calcF(K, T) < N + 1:
            T += 1
        return T


class Test(unittest.TestCase):
    def test_one(self):
        K = 3
        N = 14
        answer = 4

        result = Solution().superEggDrop(K, N)
        self.assertEqual(answer, result)
