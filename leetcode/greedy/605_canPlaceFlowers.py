import unittest
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if not flowerbed:
            return False
        flowerbed = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                n = n - 1
                flowerbed[i] = 1
            if n <= 0:
                return True
        return False


class Test(unittest.TestCase):
    def test_one(self):
        flowerbed = [1, 0, 0, 0, 1]
        n = 1
        answer = True

        result = Solution().canPlaceFlowers(flowerbed, n)
        self.assertEqual(answer, result)
