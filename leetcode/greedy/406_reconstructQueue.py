import unittest
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        print(people)
        res = []
        for item in people:
            res.insert(item[1], item)
        return res


class Test(unittest.TestCase):
    def test_one(self):
        nums = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
        answer = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]

        result = Solution().reconstructQueue(nums)
        self.assertEqual(answer, result)
