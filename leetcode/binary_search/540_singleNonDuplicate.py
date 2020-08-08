import unittest
from typing import List

'''
给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if mid % 2 == 1:
                mid -= 1
            print(nums[mid])
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]


class Test(unittest.TestCase):
    def test_one(self):
        nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
        answer = 2

        result = Solution().singleNonDuplicate(nums)
        self.assertEqual(answer, result)

    def test_one1(self):
        nums = [1, 1, 3, 3, 4, 4, 8, 8, 9]
        answer = 9

        result = Solution().singleNonDuplicate(nums)
        self.assertEqual(answer, result)

    def test_two(self):
        nums = [2, 3, 3]
        answer = 2

        result = Solution().singleNonDuplicate(nums)
        self.assertEqual(answer, result)

    def test_three(self):
        nums = [3, 3, 4]
        answer = 4

        result = Solution().singleNonDuplicate(nums)
        self.assertEqual(answer, result)

    def test_four(self):
        nums = [4]
        answer = 4

        result = Solution().singleNonDuplicate(nums)
        self.assertEqual(answer, result)
