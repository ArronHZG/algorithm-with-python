import unittest
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = ['a'] * n

        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    res[i] = nums[j]
                    break
            if res[i] == 'a':
                for j in range(i):
                    if nums[j] > nums[i]:
                        res[i] = nums[j]
                        break
        for i in range(n):
            if res[i] == 'a':
                res[i] = -1

        return res


class Test(unittest.TestCase):
    def test_one(self):
        nums = [-1,0]
        answer = [0,-1]

        result = Solution().nextGreaterElements(nums)
        self.assertEqual(answer, result)
