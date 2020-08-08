import collections
import heapq
import unittest
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)


class Test(unittest.TestCase):
    def test_one(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        answer = [1, 2]

        result = Solution().topKFrequent(nums, k)
        self.assertEqual(answer, result)
