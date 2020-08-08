import unittest
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid
                right = mid
                while left - 1 >= 0 and nums[left - 1] == target:
                    left -= 1
                while right + 1 <= len(nums) - 1 and nums[right + 1] == target:
                    right += 1
                return [left, right]
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        return [-1, -1]


class Test(unittest.TestCase):
    def test_one(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        answer = [3, 4]

        result = Solution().searchRange(nums, target)
        self.assertEqual(answer, result)
