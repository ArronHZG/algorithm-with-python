import math
import unittest
from typing import List


class Solution:
    def findMinArrowShots(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])
        print(intervals)
        cnt = i = 0
        end = -math.inf
        while i < len(intervals):
            if intervals[i][0] > end:
                end = intervals[i][1]
                cnt += 1
            i += 1
        return cnt


class Test(unittest.TestCase):
    def test_one(self):
        nums = [[10, 16], [2, 8], [1, 6], [7, 12]]
        answer = 2

        result = Solution().findMinArrowShots(nums)
        self.assertEqual(answer, result)
