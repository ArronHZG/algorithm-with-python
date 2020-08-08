import math
import unittest
from typing import List


class Solution:
    def minWindow(self, S: str, T: str) -> str:
        start = 0
        end = len(S) - 1
        i = j = 0
        while i < len(S) and j < len(T):
            if S[i] == T[j]:
                print(i, j)
                i += 1
                j += 1
            else:
                i += 1


class Test(unittest.TestCase):
    def test_one(self):
        S = "cnhczmccqouqadqtmjjzl"
        T = "mml"
        answer = "mccqouqadqtmjjzl"

        result = Solution().minWindow(S, T)
        self.assertEqual(answer, result)

    def test_two(self):
        S = "abcdebdde"
        T = "bde"
        answer = "bcde"

        result = Solution().minWindow(S, T)
        self.assertEqual(answer, result)
