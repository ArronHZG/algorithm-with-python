import unittest
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zero, two = -1, len(nums)
        i = 0
        while i < two:
            if nums[i] == 0:
                zero += 1
                nums[zero], nums[i] = nums[i], nums[zero]
                i += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                two -= 1
                nums[two], nums[i] = nums[i], nums[two]


class Test(unittest.TestCase):
    def test_one(self):
        nums = [2, 0, 2, 1, 1, 0]
        answer = [0, 0, 1, 1, 2, 2]

        Solution().sortColors(nums)
        self.assertEqual(answer, nums)
