import unittest
from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        


class Test(unittest.TestCase):
    def test_one(self):
        s = "abc"
        t = "ahbgdc"
        answer = True

        result = Solution().isSubsequence(s, t)
        self.assertEqual(answer, result)
