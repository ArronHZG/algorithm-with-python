import unittest
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(pos, target):
            if 0 == target:
                res.append(stack[:])
            elif 0 < target:
                for i in range(pos, len(candidates)):
                    if i > pos and candidates[i] == candidates[i - 1]:  # 排序后, 如果以当前节点作为子树根节点已经搜索过, 则剪枝
                        continue
                    if target - candidates[i] < 0:  # 排序后, 如果stack已经大于target, 剪枝掉后续的子树
                        break
                    stack.append(candidates[i])
                    backtrack(i + 1, target - candidates[i])
                    stack.pop()

        res = []
        stack = []
        candidates.sort()
        backtrack(0, target)
        return res


class Test(unittest.TestCase):
    def test_one(self):
        candidates = [10, 1, 2, 7, 6, 1, 5]
        target = 8
        answer = [[1, 7],
                  [1, 2, 5],
                  [2, 6],
                  [1, 1, 6]]

        result = Solution().combinationSum2(candidates, target)
        self.assertEqual(answer, result)
