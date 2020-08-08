import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(math.sqrt(c).real)

        while left <= right:
            sum = left ** 2 + right ** 2
            if sum == c:
                return True
            elif sum < c:
                left += 1
            elif sum > c:
                right -= 1
        return False