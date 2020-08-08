import unittest
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        left2right = [1] * len(ratings)
        right2left = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                left2right[i] = left2right[i - 1] + 1

        print(left2right)

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right2left[i] = right2left[i + 1] + 1
        res = 0
        for i in range(len(ratings)):
            res += max(left2right[i], right2left[i])
        return res


class Solution:
    def candy(self, ratings: List[int]) -> int:
        left2right = [1] * len(ratings)
        right2left = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                left2right[i] = left2right[i - 1] + 1

        print(left2right)

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right2left[i] = right2left[i + 1] + 1
        res = 0
        for i in range(len(ratings)):
            res += max(left2right[i], right2left[i])
        return res



class Test(unittest.TestCase):
    def test_one(self):
        nums = [1, 0, 2, 1, 2, 2]
        answer = 9

        result = Solution().candy(nums)
        self.assertEqual(answer, result)
