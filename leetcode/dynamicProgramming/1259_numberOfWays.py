import unittest
from typing import List


class Solution:
    def numberOfWays(self, num_people: int) -> int:
        memo = {0: 1, 2: 1}

        for i in range(4, num_people + 1, 2):
            tmp = 0
            for j in range(i - 2, i // 2 - 1, -2):
                tmp += 2 * (memo[j] * memo[i - j - 2])
            if i // 2 % 2 == 1:
                tmp += memo[i // 2 - 1] ** 2
            memo[i] = tmp % (10 ** 9 + 7)
        return memo[num_people]


class Test(unittest.TestCase):
    def test_one(self):
        nums = 10
        answer = 1

        result = Solution().numberOfWays(nums)
        self.assertEqual(answer, result)
