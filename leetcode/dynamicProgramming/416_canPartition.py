import unittest
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumArr = sum(nums)
        if sumArr % 1 == 1:
            return False
        halfSum = sumArr // 2
        dp = [0] * (halfSum + 1)

        for num in nums:
            for i in range(len(dp) - 1, num - 1, -1):
                dp[i] = max(dp[i], dp[i - num] + num)
            print(dp)


        if dp[-1] == halfSum:
            return True
        else:
            return False


class Test(unittest.TestCase):
    def test_one(self):
        nums = [1, 5, 11, 5]
        answer = True

        result = Solution().canPartition(nums)
        self.assertEqual(answer, result)
