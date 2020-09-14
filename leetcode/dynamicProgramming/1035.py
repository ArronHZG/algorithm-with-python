import unittest
from typing import List


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        def dfs(pos, B):
            print(num, A[pos], B)
            if pos == len(A) or len(B) == 0:
                result.append(num[0])
                return
            for i in range(len(B)):
                if A[pos] == B[i]:
                    num[0] += 1
                    dfs(pos + 1, B[i + 1:])
                    num[0] -= 1
                    return
                else:
                    dfs(pos, B[i + 1:])

        num = [0]
        result = []
        print(result)
        dfs(0, B)
        return max(result)


class Test(unittest.TestCase):
    def test_one(self):
        A = [1, 4, 2]
        B = [1, 2, 4]
        answer = 2
        result = Solution().maxUncrossedLines(A, B)
        self.assertEqual(answer, result)

    def test_two(self):
        A = [1, 3, 7, 1, 7, 5]
        B = [1, 9, 2, 5, 1]
        answer = 2
        result = Solution().maxUncrossedLines(A, B)
        self.assertEqual(answer, result)
