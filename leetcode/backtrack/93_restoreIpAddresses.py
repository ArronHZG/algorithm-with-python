import unittest
from typing import List


class Solution:
    """
    s 最短4位, 最长12位
    s 最小 0000 最大 255255255255
    s 每一段 最小为0 最大为 255
    """

    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(string):
            if len(stack) == 4:
                if string == '':
                    res.append('.'.join(stack))
                return
            for i in range(1, min(len(string) + 1, 4)):
                if i > 1 and string[0] == '0':
                    continue
                n = int(string[:i])
                if n <= 255:
                    stack.append(str(n))
                    # print('\t' * (len(stack) - 1), end='')
                    # print(string, string[:i], stack)
                    backtrack(string[i:])
                    stack.pop()

        res = []
        stack = []
        backtrack(s)
        return res


class Test(unittest.TestCase):
    def test_one(self):
        s = "101023"
        answer = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]

        result = Solution().restoreIpAddresses(s)
        self.assertEqual(answer, result)

    def test_two(self):
        s = "25525511135"
        answer = ["255.255.11.135", "255.255.111.35"]

        result = Solution().restoreIpAddresses(s)
        self.assertEqual(answer, result)
