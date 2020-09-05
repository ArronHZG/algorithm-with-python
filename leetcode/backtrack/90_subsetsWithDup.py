import unittest
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(pos):
            for i in range(pos, n):
                if i > pos and nums[i] == nums[i - 1]:
                    continue
                stack.append(nums[i])
                res.append(stack[:])
                backtrack(i + 1)
                stack.pop()

        n = len(nums)
        nums.sort()
        stack, res = [], [[]]
        backtrack(0)
        return res


class Test(unittest.TestCase):
    def test_one(self):
        nums = [1, 2, 2]
        answer = [
            [], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

        result = Solution().subsetsWithDup(nums)
        self.assertEqual(answer, result)
