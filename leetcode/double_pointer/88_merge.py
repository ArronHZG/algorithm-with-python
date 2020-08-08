import unittest
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        right = len(nums1) - 1
        while j >= 0 and i >= 0:
            if nums1[i] < nums2[j]:
                nums1[right] = nums2[j]
                j -= 1
            else:
                nums1[right] = nums1[i]
                i -= 1
            right -= 1

        nums1[:j+1] = nums2[:j+1]


class Test(unittest.TestCase):
    def test_one(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        answer = [1, 2, 2, 3, 5, 6]
        Solution().merge(nums1, m, nums2, n)
        self.assertEqual(nums1, answer)

    def test_two(self):
        nums1 = [2, 0]
        m = 1
        nums2 = [1]
        n = 1
        answer = [1, 2]
        Solution().merge(nums1, m, nums2, n)
        self.assertEqual(answer, nums1)
