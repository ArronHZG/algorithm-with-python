import heapq
import unittest
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


class Test(unittest.TestCase):
    def test_one(self):
        input = [3, 2, 1, 5, 6, 4]
        k = 2
        answer = 5

        result = Solution().findKthLargest(input, k)
        self.assertEqual(answer, result)
