import unittest
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(pos, deep):
            if deep == k:
                res.append(stack[:])
                return
            for i in range(pos, n + 1):
                stack.append(i)
                backtrack(i + 1, deep + 1)
                stack.pop()

        res = []
        stack = []
        backtrack(1, 0)
        return res


class Test(unittest.TestCase):

    def test_one(self):
        n = 4
        k = 2
        answer = [[2, 4],
                  [3, 4],
                  [2, 3],
                  [1, 2],
                  [1, 3],
                  [1, 4]]

        result = Solution().combine(n, k)
        self.assertEqual(answer, result)
