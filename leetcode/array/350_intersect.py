import unittest
from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = Counter()
        for num in nums1:
            m[num] += 1

        intersection = list()
        for num in nums2:
            if m[num] > 0:
                intersection.append(num)
                m[num] -= 1

        return intersection


class Test(unittest.TestCase):
    def test_one(self):
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        answer = [4, 9]

        result = Solution().intersect(nums1, nums2)
        self.assertEqual(answer, result)
