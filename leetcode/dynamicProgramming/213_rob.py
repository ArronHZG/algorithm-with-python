import unittest
from typing import List


def robOnce(nums: List[int]) -> int:
    dp_1 = dp_2 = 0
    for i in range(len(nums)):
        dp = max(nums[i] + dp_2, dp_1)
        dp_2 = dp_1
        dp_1 = dp
    return dp_1


class Solution:

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        return max(robOnce(nums[:-1]), robOnce(nums[1:]))


class Test(unittest.TestCase):
    def test_one(self):
        nums = [1, 9, 1, 1, 9]
        answer = 18

        result = Solution().rob(nums)
        self.assertEqual(answer, result)
