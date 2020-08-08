import unittest
from typing import List


def is_sub_string(string, d):
    i, j = 0, 0
    while i < len(string) and j < len(d):
        if string[i] == d[j]:
            i += 1
            j += 1
        else:
            j += 1

    return i == len(string)


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:

        max_str = ""

        for list_str in d:
            if is_sub_string(list_str, s):
                if len(max_str) < len(list_str) or (len(max_str) == len(list_str) and max_str > list_str):
                    max_str = list_str
        return max_str


class Test(unittest.TestCase):
    def test_one(self):
        s = "abpcplea"
        d = ["ale", "apple", "monkey", "plea"]
        answer = "apple"

        result = Solution().findLongestWord(s, d)
        self.assertEqual(result, answer)

    def test_two(self):
        s = "bab"
        d = ["ba", "ab", "a", "b"]
        answer = "ab"

        result = Solution().findLongestWord(s, d)
        self.assertEqual(result, answer)
