import unittest
from typing import List


class Solution:
    def qpow(self, x, n, m):
        ans = 1
        while n > 0:
            if n & 1 == 1:
                ans = ans * x % m
            x = x * x % m
            n >>= 1
        return ans

    def superPow(self, a: int, b: List[int]) -> int:
        res = 1
        for i in b:
            res = self.qpow(res, 10, 1337) * self.qpow(a, i, 1337)
        return res % 1337


class Test(unittest.TestCase):
    def test_one(self):
        answer = 1024
        result = Solution().superPow(2, [8])
        self.assertEqual(answer, result)
