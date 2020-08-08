import unittest
from typing import List


class Solution:
    def convertToBase7(self, num: int) -> str:
        base7 = []
        isNegative = False
        if num < 0:
            isNegative = True
            num = -num
        while num >= 7:
            base7.append(str(num % 7))
            num = num // 7
        base7.append(str(num))
        if isNegative:
            base7.append('-')
        base7.reverse()
        return ''.join(base7)


class Test(unittest.TestCase):
    def test_one(self):
        nums = 100
        answer = "202"

        result = Solution().convertToBase7(nums)
        self.assertEqual(answer, result)
