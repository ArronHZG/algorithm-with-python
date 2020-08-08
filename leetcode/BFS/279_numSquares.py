import math
import unittest
from collections import deque
from typing import List


class Solution:
    def numSquares(self, n: int) -> int:
        q = deque()
        visited = set()
        q.append(n)
        res = 0
        while q:
            res += 1
            for _ in range(len(q)):
                top = q.popleft()
                for i in range(int(math.sqrt(top)), 0, -1):
                    x = top - i ** 2
                    if x == 0:
                        return res
                    elif x not in visited:
                        visited.add(x)
                        q.append(x)


class Test(unittest.TestCase):
    def test_one(self):
        nums = 1000000000
        answer = 2

        result = Solution().numSquares(nums)
        self.assertEqual(answer, result)
