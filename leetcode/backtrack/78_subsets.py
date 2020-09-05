import unittest
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def backtrack(pos, deep):
            if deep <= n:
                res.append(stack[:])
            for i in range(pos, n):
                stack.append(nums[i])
                print(pos, deep, stack)
                backtrack(i + 1, deep + 1)
                stack.pop()

        res = []
        stack = []
        backtrack(0, 0)
        return res


class Test(unittest.TestCase):
    def test_one(self):
        nums = [1, 2, 3]
        answer = [[3],
                  [1],
                  [2],
                  [1, 2, 3],
                  [1, 3],
                  [2, 3],
                  [1, 2],
                  []]

        result = Solution().subsets(nums)
        self.assertEqual(answer, result)
