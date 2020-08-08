import unittest
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for i in range(1,len(nums)):
            if nums[i] >  nums


class Test(unittest.TestCase):
    def test_one(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        answer = 4

        result = Solution().(nums)
        self.assertEqual(answer, result)
