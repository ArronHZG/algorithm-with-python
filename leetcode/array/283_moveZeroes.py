from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fast = 0
        slow = -1
        while fast < len(nums):
            if nums[fast] != 0:
                slow += 1
                nums[fast], nums[slow] = nums[slow], nums[fast]
            fast += 1
