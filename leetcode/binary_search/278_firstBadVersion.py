import unittest
from typing import List

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

answer = 4


def isBadVersion(version):
    if version >= answer:
        return True
    return False


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n  # 确认区间为[]
        while left < right:
            mid = left + (right - left) // 2
            print(f"left {left} mid {mid} right {right}")
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


class Test(unittest.TestCase):
    def test_one(self):
        result = Solution().firstBadVersion(5)
        self.assertEqual(answer, result)
