import unittest
from typing import List


# class Solution:
#     def findContentChildren(self, children: List[int], cookies: List[int]) -> int:
#         children = sorted(children)
#         cookies = sorted(cookies)
#         i = j = res = 0
#         while i < len(children) and j < len(cookies):
#             if children[i] <= cookies[j]:
#                 i += 1
#                 j += 1
#                 res += 1
#             else:
#                 j += 1
#         return res


class Solution:
    def findContentChildren(self, children: List[int], cookies: List[int]) -> int:
        children = sorted(children)
        cookies = sorted(cookies)

        i, j = len(children) - 1, len(cookies) - 1
        res = 0
        while i >= 0 and j >= 0:
            while i >= 0:
                if cookies[j] >= children[i]:
                    res += 1
                    i -= 1
                    break
                else:
                    i -= 1
            j -= 1
        return res


class Test(unittest.TestCase):
    def test_one(self):
        children, cookies = [10, 9, 8, 7], [5, 6, 7, 8]
        answer = 2

        result = Solution().findContentChildren(children, cookies)
        self.assertEqual(answer, result)
