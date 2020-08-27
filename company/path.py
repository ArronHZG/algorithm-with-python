import unittest
from typing import List


def minPathSum(grid):
    n = len(grid[0])
    m = len(grid)
    layer_id = 0
    layer = grid[0]
    while layer_id <= m - 2:
        dp = [[] for _ in range(n)]
        for i, a in enumerate(layer):
            for j in range(n):
                if j == i:
                    dp[j].append(layer[i] + grid[layer_id + 1][j])
                elif j > i:
                    k = i
                    tmp = layer[i]
                    while k <= j:
                        tmp += grid[layer_id + 1][k]
                        k += 1
                    dp[j].append(tmp)
                elif j < i:
                    k = i
                    tmp = layer[i]
                    while k >= j:
                        tmp += grid[layer_id + 1][k]
                        k -= 1
                    dp[j].append(tmp)
        layer = [min(d) for d in dp]
        layer_id += 1
    return min(layer)


# class Test(unittest.TestCase):
#     def test_one(self):
#         nums = [[20, 30, 1, 2],
#                 [2, 2, 2, 40],
#                 [3, 30, 30, 20]]
#         answer = 10
#
#         result = Solution().minPathSum(nums)
#         self.assertEqual(answer, result)
if __name__ == '__main__':
    # 读取第一行的n
    line = input().strip().split(' ')
    n, m = [int(x) for x in line]
    nums = []
    for i in range(n):
        line = input().strip().split(' ')
        ll = [int(x) for x in line]
        nums.append(ll)
    print(minPathSum(nums))
