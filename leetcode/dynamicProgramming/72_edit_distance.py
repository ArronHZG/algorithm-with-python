import unittest


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for j in range(m + 1):
            dp[0][j] = j
        for i in range(n + 1):
            dp[i][0] = i
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[-1][-1]


class Test(unittest.TestCase):
    def test_one(self):
        word1 = 'horse'
        word2 = 'ros'
        answer = 3

        result = Solution().minDistance(word1, word2)
        self.assertEqual(answer, result)
