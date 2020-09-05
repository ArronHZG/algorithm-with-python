import unittest
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1   # 左闭右闭区间，如果用右开区间则不方便判断右值
        while left < right:              # 循环不变式，如果left == right，则循环结束
            mid = (left + right) >> 1    # 地板除，mid更靠近left
            print(f"left {left} mid {mid} right {right}")
            if nums[mid] > nums[right]:  # 中值 > 右值，最小值在右半边，收缩左边界
                left = mid + 1           # 因为中值 > 右值，中值肯定不是最小值，左边界可以跨过mid
            else:                        # 明确中值 < 右值，最小值在左半边，收缩右边界
                right = mid              # 因为中值 < 右值，中值也可能是最小值，右边界只能取到mid处

        return nums[left]                # 循环结束，left == right，最小值输出nums[left]或nums[right]均可


class Test(unittest.TestCase):
    def test_one(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        answer = 0

        result = Solution().findMin(nums)
        self.assertEqual(answer, result)

    def test_two(self):
        nums = [1, 2, 3]
        answer = 1

        result = Solution().findMin(nums)
        self.assertEqual(answer, result)

    def test_three(self):
        nums = [1, 2, 0]
        answer = 0

        result = Solution().findMin(nums)
        self.assertEqual(answer, result)
