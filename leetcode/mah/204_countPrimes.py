import unittest
from typing import List
import numpy as np
from numba import njit


class Solution:

    def countPrimes(self, n):
        """
        nums = 200000000
        13.018s
        求n以内的所有质数个数（纯python代码）
        """
        # 最小的质数是 2
        if n < 2:
            return 0

        isPrime = [1] * n
        isPrime[0] = isPrime[1] = 0  # 0和1不是质数，先排除掉

        print(isPrime)

        # 埃式筛，把不大于根号n的所有质数的倍数剔除
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                isPrime[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)
            print(isPrime)

        return sum(isPrime)

class SolutionNumpy:
    def countPrimes(self, n):
        """
        nums = 200000000
        1.581s
        nums = 1000000000
        9.006s
        """
        # 最小的质数是 2
        if n < 2:
            return 0

        isPrime = np.ones(n, dtype=np.bool_)
        isPrime[0] = isPrime[1] = 0

        for i in np.arange(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                isPrime[i * i:n:i] = 0

        return int(np.sum(isPrime))


@njit
def countPrimes(n):
    """
    nums = 200000000
    2.018s
    nums = 1000000000
    8.956s
    """
    # 最小的质数是 2
    isPrime = np.ones(n, dtype=np.bool_)
    isPrime[0] = isPrime[1] = 0
    for i in np.arange(2, int(n ** 0.5) + 1):
        if isPrime[i]:
            isPrime[i * i:n:i] = 0
    return int(np.sum(isPrime))


class Test(unittest.TestCase):
    def test_one(self):
        nums = 1000000000
        answer = 50847534

        result = SolutionNumpy().countPrimes(nums)
        self.assertEqual(answer, result)

    def test_two(self):
        nums = 20
        answer = 4

        result = Solution().countPrimes(nums)
        self.assertEqual(answer, result)
