import unittest
from typing import List


class Solution:
    """
    先做转置, 再做翻转
    """

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n // 2):
            for j in range(n):
                matrix[j][i], matrix[j][n - i - 1] = matrix[j][n - i - 1], matrix[j][i]


class Test(unittest.TestCase):
    def test_one(self):
        nums = 8
        answer = 2

        result = Solution().(nums)
        self.assertEqual(answer, result)
