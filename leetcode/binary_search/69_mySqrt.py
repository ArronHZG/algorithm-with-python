import unittest
from typing import List


class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = (right + left) // 2
            if mid ** 2 <= x:
                left = mid + 1
            else:
                right = mid - 1
        return right


class Test(unittest.TestCase):
    def test_one(self):
        num = 8
        answer = 2

        result = Solution().mySqrt(num)
        self.assertEqual(answer, result)

    def test_two(self):
        num = 0
        answer = 0

        result = Solution().mySqrt(num)
        self.assertEqual(answer, result)

    def test_three(self):
        num = 1
        answer = 1

        result = Solution().mySqrt(num)
        self.assertEqual(answer, result)

    def test_four(self):
        num = 2
        answer = 1

        result = Solution().mySqrt(num)
        self.assertEqual(answer, result)
