import unittest
from typing import List


class Solution:
    def numberOfWays(self, num_people: int) -> int:


class Test(unittest.TestCase):
    def test_one(self):
        nums = 8
        answer = 14

        result = Solution().numberOfWays(nums)
        self.assertEqual(answer, result)