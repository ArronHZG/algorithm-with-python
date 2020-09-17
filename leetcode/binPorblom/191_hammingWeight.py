import unittest
from typing import List


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            if n & 1 == 1:
                count += 1
            n //= 10
        return count


class Test(unittest.TestCase):
    def test_one(self):
        nums = 1011
        answer = 3

        result = Solution().hammingWeight(nums)
        self.assertEqual(answer, result)
