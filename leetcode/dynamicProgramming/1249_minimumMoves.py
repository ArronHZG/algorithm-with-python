import math
import unittest
from functools import lru_cache
from typing import List, Tuple
"""
hard
"""

class SolutionOne:
    """
    动态规划
    len(s) >=1
    dp(s)表示s最少经过多少次回文删除
    现在看怎么求dp(s), 看最后一个字符，要么出现在最后剩余的回文中，要么就不在最后剩余的回文中

        不在最后剩余的回文 dp(s) = dp(s[:-1]) + 1

        如果最后一个字符在最后剩余的回文中，那必然要和前面一个相同的字符位置i配在一起，然后把中间的一段通过删除变成回文，
        这样就找到了一个规模更小的子问题，另外因为是最后一个字符保留了下来，那i位置前面的段只能删掉，前面段删掉需要的删除操作次数
        就是dp(s[:i]), 又是一个子问题，i的位置可能有多个，取总删除次数最少的一个
        dp(s) = min i dp(s[:i]) + dp(s[i+1:-1])
        特殊情况 i = 0 时, dp(s) = dp(s[i+1:-1]) 需要单独处理
        因为设置11, 121 都是回文数字, 去掉边界后, [] , [1] 删除操作都需要1次, 保证[]代表的回文数, 而不是空字符

        最后在dp(s) 取上述结果最小

    """

    def minimumMovesDict(self, arr: List[int]) -> int:
        # 返回最少经过多少次删除可以让s变成一个回文
        def dp(tu):
            if tu in memo.keys():
                return memo[tu]
            if len(tu) <= 1:
                ans = 1
            else:
                ans = 1 + dp(tu[:-1])
                if tu[0] == tu[-1]:
                    ans = min(ans, dp(tu[1:-1]))
                for i in range(1, len(tu) - 1):
                    if tu[i] == tu[-1]:
                        ans = min(ans, dp(tu[:i]) + dp(tu[i + 1:-1]))
            memo[tu] = ans
            return ans

        memo = dict()
        return dp(tuple(arr))

    def minimumMoves(self, arr: List[int]) -> int:
        """
        1628 ms 32.7 MB
        """

        # 返回最少经过多少次删除可以让s变成一个回文
        @lru_cache(maxsize=12800)
        def dp(tu):
            if len(tu) <= 1:
                ans = 1
            else:
                ans = 1 + dp(tu[:-1])
                if tu[0] == tu[-1]:
                    ans = min(ans, dp(tu[1:-1]))
                for i in range(1, len(tu) - 1):
                    if tu[i] == tu[-1]:
                        ans = min(ans, dp(tu[:i]) + dp(tu[i + 1:-1]))
            return ans

        return dp(tuple(arr))


def show(dp):
    for line in dp:
        print(line)
    print('-' * 20)


class SolutionTwo:
    """
    区间dp，我们令f(i,j)代表删除区间[i,j]的最小值（即最小删除次数），那么可得以下递推公式：

    f(i,j) = min    f(i+1,j-1), f(i,k)+f(k+1,j)     arr[i] == arr[j]    i<=k<j
    f(i,j) = min    f(i,j), f(i,k)+f(k+1,j)         arr[i]!=arr[j]      i<=k<j

    """

    def minimumMoves(self, arr: List[int]):
        """
        4080 ms	13.7 MB
        """
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for j in range(1, n):
            for i in range(j - 1, -1, -1):
                # 判断两个数是否为回文数
                if i == j - 1:
                    dp[i][j] = 1 if arr[i] == arr[j] else 2
                    continue
                # 大于等于三个数
                min_num = math.inf
                if arr[i] == arr[j]:
                    min_num = dp[i + 1][j - 1]
                for k in range(i, j):
                    min_num = min(min_num, dp[i][k] + dp[k + 1][j])
                dp[i][j] = min_num
        return dp[0][-1]


class Solution:
    """
    dp(i,j) 表示 arr[i:j] 删除所需要的次数
    出现回文数才可能减少删除的次数, 也就是说要尽量找到相同的数字, 然后在内部删除, 使之成为回文数

    dp(i,j) = min(dp(i,k) + dp(k+1,j)) arr[i] == arr[k]

    dp(i,k) = max(dp(i+1,k-1),1)
    """

    def minimumMovesDP(self, arr: List[int]) -> int:
        def helper(left, right):
            if left > right:
                return dp[left][right]
            if left == right:
                dp[left][right] = 1
                return dp[left][right]
            if dp[left][right] != 0:
                return dp[left][right]
            dp[left][right] = helper(left + 1, right) + 1
            print(left, right)
            show(dp)
            for k in range(left + 1, right + 1):
                if arr[k] == arr[left]:
                    dp[left][right] = min(dp[left][right], max(helper(left + 1, k - 1), 1) + helper(k + 1, right))
                    print(left, right)
                    show(dp)
            return dp[left][right]

        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        return helper(0, n - 1)

    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)

        @lru_cache(maxsize=12800)
        def dp(left, right):
            if left > right:
                return 0
            if left == right:
                return 1
            min_num = dp(left + 1, right) + 1
            for k in range(left + 1, right + 1):
                if arr[k] == arr[left]:
                    min_num = min(min_num, max(dp(left + 1, k - 1), 1) + dp(k + 1, right))
            return min_num

        return dp(0, n - 1)


class Test(unittest.TestCase):
    def test_1(self):
        nums = [1, 3, 1]
        answer = 1

        result = Solution().minimumMoves(nums)
        self.assertEqual(answer, result)

    def test_2(self):
        nums = [1, 1]
        answer = 1

        result = Solution().minimumMoves(nums)
        self.assertEqual(answer, result)

    def test_one(self):
        nums = [1, 3, 4, 1, 5]
        answer = 3

        result = Solution().minimumMoves(nums)
        self.assertEqual(answer, result)

    def test_two(self):
        nums = [16, 13, 13, 10, 12]
        answer = 4

        result = Solution().minimumMoves(nums)
        self.assertEqual(answer, result)
