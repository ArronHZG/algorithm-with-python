import unittest
from typing import List


class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for _ in range(n - 1):  # 控制循环次数
            i, tmp = 0, ''
            for j, c in enumerate(res):
                if c != res[i]:
                    tmp += str(j - i) + res[i]
                    i = j
            res = tmp + str(len(res) - i) + res[-1]
        return res


class Test(unittest.TestCase):
    def test_one(self):
        nums = 5
        answer = '111221'

        result = Solution().countAndSay(nums)
        self.assertEqual(answer, result)
