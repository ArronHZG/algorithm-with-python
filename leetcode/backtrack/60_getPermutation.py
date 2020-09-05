import itertools
import math
import unittest
from typing import List


class SolutionOne:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [x for x in range(1, n + 1)]
        k_list = list(itertools.permutations(nums))[k - 1]
        return ''.join([str(x) for x in k_list])


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def backtrack(nums, pos):
            if not nums:
                return
            fact = math.factorial(len(nums) - 1)
            index = pos // fact
            res.append(str(nums[index]))
            backtrack(nums[:index] + nums[index + 1:], (pos - fact) % fact)

        nums = [x for x in range(1, n + 1)]
        res = []
        backtrack(nums, k - 1)
        return ''.join(res)


class Test(unittest.TestCase):
    def test_one(self):
        n = 4
        k = 9
        answer = '2314'
        result = Solution().getPermutation(n, k)
        self.assertEqual(answer, result)
