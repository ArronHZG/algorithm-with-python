"""
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:

可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/non-overlapping-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
import math
import unittest
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])

        print(intervals)
        remove = 0
        i = len(intervals) - 1
        left = math.inf
        while i >= 0:
            if left >= intervals[i][1]:
                left = intervals[i][0]
            else:
                left = max(intervals[i][0], left)
                remove += 1
            i -= 1

        return remove


class Test(unittest.TestCase):
    def test_one(self):
        nums = [[1, 2], [2, 3], [3, 4], [1, 3]]
        answer = 1

        result = Solution().eraseOverlapIntervals(nums)
        self.assertEqual(answer, result)
