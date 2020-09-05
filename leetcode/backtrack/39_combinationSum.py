import unittest
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(pos, target):
            if 0 == target:
                res.append(stack[:])
            elif 0 < target:
                for i in range(pos, len(candidates)):
                    if target - candidates[i] < 0:
                        break
                    stack.append(candidates[i])
                    backtrack(i, target - candidates[i])
                    stack.pop()

        res = []
        stack = []
        candidates.sort()
        backtrack(0, target)
        return res


class Test(unittest.TestCase):
    def test_one(self):
        candidates = [2, 3, 6, 7]
        target = 7
        answer = [[2, 2, 3], [7]]

        result = Solution().combinationSum(candidates, target)
        self.assertEqual(answer, result)
