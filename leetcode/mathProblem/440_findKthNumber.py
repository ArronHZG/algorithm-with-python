import heapq
import unittest
from typing import List


def getCount(prefix, n):
    """
    下一个前缀的起点减去当前前缀的起点
    :param prefix: 前缀
    :param n: 上界
    :return:
    """
    nextPrefix = prefix + 1  # 下一个前缀
    count = 0
    while prefix <= n:
        count += min(n + 1, nextPrefix) - prefix  # 下一个前缀的起点减去当前前缀的起点
        prefix *= 10
        nextPrefix *= 10

        # 如果说刚刚prefix是1，next是2，那么现在分别变成10和20
        # 为前缀的子节点增加10个，十叉树增加一层, 变成了两层
        # 如果说现在prefix是10，next是20，那么现在分别变成100和200，
        # 为前缀的子节点增加100个，十叉树又增加了一层，变成了三层

    return count


class Solution:

    def findKthNumber(self, n: int, k: int) -> int:
        prefix = 1
        p = 1  # 作为一个指针，指向当前所在位置，当p==k时，也就是到了排位第k的数
        print(f"prefix {prefix}  count {p}")
        while p < k:
            # 确定指定前缀下所有子节点数
            curCount = getCount(prefix, n)
            print(f"prefix {prefix}  p {p} curCount {curCount}")
            # 第k个数在当前前缀下
            if curCount + p > k:
                prefix *= 10
                p += 1  # 把指针指向了第一个子节点的位置，比如11乘10后变成110，指针从11指向了110
            else:
                prefix += 1
                p += curCount

        return prefix


class Test(unittest.TestCase):
    def test_one(self):
        nums = 200
        k = 40
        answer = 134
        result = Solution().findKthNumber(nums, k)
        self.assertEqual(answer, result)
