import unittest
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        left, right = 0, len(letters) - 1
        while left <= right:
            mid = (right + left) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return letters[left % len(letters)]


class Test(unittest.TestCase):
    def test_one(self):
        letters = ["c", "f", "j"]
        target = "a"
        answer = "c"

        result = Solution().nextGreatestLetter(letters, target)
        self.assertEqual(answer, result)

    def test_two(self):
        letters = ["c", "f", "j"]
        target = "k"
        answer = "c"

        result = Solution().nextGreatestLetter(letters, target)
        self.assertEqual(answer, result)
