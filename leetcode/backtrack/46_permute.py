import itertools
import unittest
from typing import List


class SolutionOne:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first):
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                nums[i], nums[first] = nums[first], nums[i]
                backtrack(first + 1)
                nums[i], nums[first] = nums[first], nums[i]

        n = len(nums)
        res = []
        backtrack(0)
        return res


class Test(unittest.TestCase):
    def test_one(self):
        nums = [1, 2, 3]
        answer = [[1, 2, 3],
                  [1, 3, 2],
                  [2, 1, 3],
                  [2, 3, 1],
                  [3, 2, 1],
                  [3, 1, 2]]

        result = Solution().permute(nums)
        self.assertEqual(answer, result)
