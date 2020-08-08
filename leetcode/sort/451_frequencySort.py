import collections
import heapq
import unittest
from collections import Counter


#
# class Solution:
#     def frequencySort(self, s: str) -> str:
#         # Counter
#         return ''.join([i * j for i, j in collections.Counter(s).most_common()])


class Solution:
    def frequencySort(self, s: str) -> str:
        # 大顶堆
        countFrequency = collections.defaultdict(int)
        for i in s:
            countFrequency[i] += 1
        lst = []
        for i in countFrequency:
            for j in range(countFrequency[i]):
                heapq.heappush(lst, (-countFrequency[i], i))
                print(lst)

        return ''.join([heapq.heappop(lst)[1] for _ in range(len(s))])


class Test(unittest.TestCase):
    def test_one(self):
        string = "tree"
        answer = "eert"

        result = Solution().frequencySort(string)
        self.assertEqual(answer, result)
