import unittest
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp_1 = dp_2 = 0
        for i in range(len(nums)):
            dp = max(nums[i] + dp_2, dp_1)
            dp_2 = dp_1
            dp_1 = dp
        return dp_1

    # class Test(unittest.TestCase):
    #     def test_one(self):
    #         nums = [1, 9, -1, -1, -1, 9]
    #         answer = 18
    #
    #         result = Solution().rob(nums)
    #         self.assertEqual(answer, result)


def rob(nums: List[int]) -> int:
    dp_1 = dp_2 = 0
    for i in range(len(nums)):
        dp = max(nums[i] + dp_2, dp_1, nums[i])
        dp_2 = dp_1
        dp_1 = dp
    return dp_1


nums = [int(x) for x in input().split(',')]

print(rob(nums))
