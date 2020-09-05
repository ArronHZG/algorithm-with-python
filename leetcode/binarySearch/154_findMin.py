import unittest
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            print(f"left {left} mid {mid} right {right}")
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1

        return nums[left]


class Test(unittest.TestCase):
    def test_one(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        answer = 0

        result = Solution().findMin(nums)
        self.assertEqual(answer, result)

    def test_two(self):
        nums = [1, 1, 2, 2, 3]
        answer = 1

        result = Solution().findMin(nums)
        self.assertEqual(answer, result)

    def test_three(self):
        nums = [1, 1, 1, 0, 0, 0, 0]
        answer = 0

        result = Solution().findMin(nums)
        self.assertEqual(answer, result)

    def test_four(self):
        nums = [1, 1, 1, 0, 1]
        answer = 0

        result = Solution().findMin(nums)
        self.assertEqual(answer, result)

    def test_five(self):
        nums = [1, 1, 2, 0, 0, 1]
        answer = 0

        result = Solution().findMin(nums)
        self.assertEqual(answer, result)

    def test_six(self):
        nums = [3, 3, 1, 3]
        answer = 1

        result = Solution().findMin(nums)
        self.assertEqual(answer, result)

    def test_seven(self):
        nums = [3, 3, 3, 3]
        answer = 3

        result = Solution().findMin(nums)
        self.assertEqual(answer, result)

    def test_eight(self):
        nums = [3, 1, 3, 3, 3]
        answer = 1

        result = Solution().findMin(nums)
        self.assertEqual(answer, result)
