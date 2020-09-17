from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        maxAns = nums[0]
        for x in nums:
            pre = max(pre + x, x)
            maxAns = max(maxAns, pre)
        return maxAns
