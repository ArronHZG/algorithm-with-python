import unittest
from collections import defaultdict
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0: -1}
        count = 0
        max_len = 0
        for index, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1

            if count not in d.keys():
                d[count] = index
            else:
                max_len = max(max_len, index - d[count])

        return max_len


class Test(unittest.TestCase):
    def test_one(self):
        nums = [0, 1, 0, 0, 1, 1, 0]
        answer = 6

        result = Solution().findMaxLength(nums)
        self.assertEqual(answer, result)


class Test(unittest.TestCase):
    def test_one(self):
        nums = [0, 1]
        answer = 2

        result = Solution().findMaxLength(nums)
        self.assertEqual(answer, result)
