import unittest
from typing import List

"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:

    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            print(f"left {left} mid {mid} right {right}")
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return left

    def find(self, nums: List[int], target: int, left, right):

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        mid = self.findMin(nums)
        if nums[mid] <= target <= nums[-1]:
            res = self.find(nums, target, mid, len(nums) - 1)
        elif nums[0] <= target <= nums[mid - 1]:
            res = self.find(nums, target, 0, mid - 1)
        else:
            res = -1

        return res


class Test(unittest.TestCase):
    def test_one(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        answer = 4

        result = Solution().search(nums, target)
        self.assertEqual(answer, result)

    def test_two(self):
        nums = [1, 2, 3]
        target = 2
        answer = 1

        result = Solution().search(nums, target)
        self.assertEqual(answer, result)

    def test_three(self):
        nums = [1, 2, 0]
        target = 1
        answer = 0

        result = Solution().search(nums, target)
        self.assertEqual(answer, result)
