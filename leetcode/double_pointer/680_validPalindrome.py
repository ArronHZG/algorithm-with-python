import unittest
from typing import List


def isPalindrome(s):
    return s == s[::-1]


class Solution:

    def validPalindrome(self, s: str) -> bool:

        if not s:
            return True
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return isPalindrome(s[left + 1: right + 1]) or isPalindrome(s[left: right])
        return True


class Test(unittest.TestCase):
    def test_one(self):
        input = "aba"
        answer = True

        result = Solution().validPalindrome(input)
        self.assertEqual(result, answer)
