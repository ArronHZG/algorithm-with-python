import unittest
from typing import List


class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False

        if num == 1 or num == 2 or num == 3 or num == 5:
            return True

        if (num % 2 == 0 and self.isUgly(num // 2)) or (
                num % 3 == 0 and self.isUgly(num // 3)) or (
                num % 5 == 0 and self.isUgly(num // 5)):
            return True

        return False


class Test(unittest.TestCase):
    def test_one(self):
        nums = 8
        answer = True

        result = Solution().isUgly(nums)
        self.assertEqual(answer, result)
