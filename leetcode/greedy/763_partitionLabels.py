import unittest
from typing import List


class Solution(object):
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        print(last)
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1

        return ans


class Test(unittest.TestCase):
    def test_one(self):
        nums = "ababcbacadefegdehijhklij"
        answer = [9, 7, 8]

        result = Solution().partitionLabels(nums)
        self.assertEqual(answer, result)
