import unittest
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(len(dp)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        print(dp)
        return max(dp)


class Test(unittest.TestCase):
    def test_one(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        answer = 4
        result = Solution().lengthOfLIS(nums)
        self.assertEqual(answer, result)

    def test_two(self):
        nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
        answer = 6
        result = Solution().lengthOfLIS(nums)
        self.assertEqual(answer, result)
