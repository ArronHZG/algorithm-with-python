import math
from collections import defaultdict
from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
            points.sort(key=lambda P: P[0] ** 2 + P[1] ** 2)
            return points[:K]


points = [[1, 3], [-2, 2], [5, 3], [-2, 3], [2, 1], [-1, 2]]
K = 1

ans = Solution().kClosest(points, K)
print(ans)
