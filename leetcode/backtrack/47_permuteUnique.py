import itertools
import unittest
from typing import List


class SolutionOne:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first):
            if first == n and nums[:] not in res:
                res.append(nums[:])
            for i in range(first, n):
                nums[i], nums[first] = nums[first], nums[i]
                backtrack(first + 1)
                nums[i], nums[first] = nums[first], nums[i]

        n = len(nums)
        res = []
        backtrack(0)
        return res


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def backtrack(first):
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                if i > first and nums[i] == nums[first]:
                    print(first, i, nums)
                    continue
                nums[i], nums[first] = nums[first], nums[i]
                backtrack(first + 1)
                nums[i], nums[first] = nums[first], nums[i]

        sorted(nums)
        n = len(nums)
        res = []
        backtrack(0)
        return res


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def recur(nums, temp):
            if not nums:
                res.append(temp)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:  # 每当进入新的构成，先考虑该构成的首字符是否和上一个一样。
                    continue
                recur(nums[:i] + nums[i + 1:], temp + [nums[i]])  # nums[:i]+nums[i+1:] 避免了重复利用。

        nums.sort()  # 数组先排序
        res = []
        recur(nums, [])
        return res


class Test(unittest.TestCase):
    def test_one(self):
        nums = [1, 1, 2]
        answer = [[1, 1, 2],
                  [1, 2, 1],
                  [2, 1, 1]]

        result = Solution().permuteUnique(nums)
        self.assertEqual(answer, result)

    def test_two(self):
        nums = [1, 1, 2, 2]
        answer = [[1, 1, 2, 2],
                  [1, 2, 1, 2],
                  [1, 2, 2, 1],
                  [2, 1, 1, 2],
                  [2, 1, 2, 1],
                  [2, 2, 1, 1]]

        result = Solution().permuteUnique(nums)
        self.assertEqual(answer, result)
