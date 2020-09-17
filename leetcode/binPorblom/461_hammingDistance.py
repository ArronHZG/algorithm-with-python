import unittest
from typing import List


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = x ^ y

        count = 0
        while a != 0:
            print(bin(a))
            count += a & 1
            a >>= 1
        return count


class Test(unittest.TestCase):
    def test_one(self):
        x = 1
        y = 4
        answer = 2

        result = Solution().hammingDistance(x, y)
        self.assertEqual(answer, result)
