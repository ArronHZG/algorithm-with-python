import unittest
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


class Test(unittest.TestCase):
    def test_one(self):
        nums = [1, 2, 3]
        answer = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
        ]

        result = Solution().permute(nums)
        self.assertEqual(answer, result)
