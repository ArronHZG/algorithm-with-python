import unittest
from collections import deque
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        dq = deque()
        dq.append([sr, sc])
        old = image[sr][sc]
        if newColor == old:
            return image
        while dq:
            for _ in range(len(dq)):
                x, y = dq.popleft()
                image[x][y] = newColor
                for order in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    t_x = x + order[0]
                    t_y = y + order[1]
                    if 0 <= t_x < len(image) and 0 <= t_y < len(image[-1]) and image[t_x][t_y] == old:
                        dq.append([t_x, t_y])
        return image


class Test(unittest.TestCase):
    def test_one(self):
        image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        sr = 1
        sc = 1
        newColor = 2
        answer = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

        result = Solution().floodFill(image, sr, sc, newColor)
        self.assertEqual(answer, result)
