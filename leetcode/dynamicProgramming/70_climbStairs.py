class Solution:
    def climbStairs(self, n: int) -> int:
        dp_1 = 1
        dp_2 = 1
        dp_3 = 1
        for i in range(2, n + 1):
            dp_3 = dp_1 + dp_2
            dp_1 = dp_2
            dp_2 = dp_3
        return dp_3
