import unittest
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """


class Test(unittest.TestCase):
    def test_one(self):
        nums = [['X', 'X', 'X', 'X'],
                ['X', 'O', 'O', 'X'],
                ['X', 'X', 'O', 'X'],
                ['X', 'O', 'X', 'X']]

    answer = 2

    result = Solution().(nums)
    self.assertEqual(answer, result)
