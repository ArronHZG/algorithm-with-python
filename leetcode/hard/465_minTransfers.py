import math
import unittest
from collections import Counter
from functools import lru_cache
from typing import List


class SolutionOne:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        person = Counter()
        for x, y, z in transactions:
            person[x] -= z
            person[y] += z
        # 账号
        accounts = list(person.values())

        print(accounts)

        res = float("inf")

        def dfs(i, cnt):
            nonlocal res
            # 全局变量退出递归
            if cnt >= res:
                return
            # 账号为0不考虑
            while i < len(accounts) and accounts[i] == 0:
                i += 1
            # 遍历完
            if i == len(accounts):
                res = min(res, cnt)
                return
            for j in range(i + 1, len(accounts)):
                if accounts[i] * accounts[j] < 0:
                    accounts[j] += accounts[i]
                    dfs(i + 1, cnt + 1)
                    accounts[j] -= accounts[i]

        dfs(0, 0)
        return res


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        """
        '''
        把每个人看成一个图里面的节点，借钱给别人和别人借钱给自己分别对应节点
        的出边和入边，权值分别对应正的和负的，每一个人统计了自己的入边和出
        边之后，要么权值和是正的，要么权值和是负的

        权值和是0人不亏不赚直接去掉这些节点
        权值和是正的节点需要分批次把自己的权值分给权值是负值的节点，
        最后每个节点权值和都等于0，债就还完了，

        其实就是把负数的节点看成容量是其权值和相反数的桶，权值是正数的节点把自己的权值往桶里面放问最少的放置次数是多少

        深度优先搜索, 回溯法, 剪枝


        可以转换成一个简单的DP递推问题，每次就看持有权值最多的节点，当前的权值要放哪个桶里面去，枚举可能放置的桶，进而可以
        枚举出下一步可能出现的桶容量状态和正数节点的剩余数值状态，明显的用DP来求桶空状态到桶满状态的最少状态转移次数，记忆化递归就可以了
        '''


        作者：hao-shou-bu-juan
        链接：https://leetcode-cn.com/problems/optimal-account-balancing/solution/python-dong-tai-gui-hua-ji-yi-hua-di-gui-ji-bai-90/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        :param transactions:
        :return:
        """
        c = Counter()
        for a, b, val in transactions:
            c[a] -= val
            c[b] += val

        l1 = [val for val in c.values() if val > 0]
        l2 = [-val for val in c.values() if val < 0]
        l1.sort(reverse=True)
        l2.sort(reverse=True)
        return self.solve(tuple(l1), tuple(l2))

    # 正数权值节点状态是l1, 桶容量状态是l2情况下的最少转移次数
    @lru_cache(typed=False, maxsize=128000000)
    def solve(self, l1: tuple, l2: tuple) -> int:
        print(l1)
        print(l2)
        if sum(l1) == 0:
            return 0
        ans = math.inf
        l1, l2 = list(l1), list(l2)
        for i in range(len(l2)):
            if l2[i] > 0:
                sub = min(l1[0], l2[i])
                l1[0] -= sub
                l2[i] -= sub
                ans = min(ans, 1 + self.solve(tuple(sorted(l1, reverse=True)), tuple(sorted(l2, reverse=True))))
                l1[0] += sub
                l2[i] += sub
                print('')
        return ans


class Test(unittest.TestCase):
    def test_one(self):
        nums = [[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]

        answer = 1
        #
        # result = Solution().minTransfers(nums)
        # self.assertEqual(answer, result)

        l1 = (4, 3, 2, 1)
        l2 = (5, 4, 1)

        a = Solution().solve(l1, l2)
        print(a)
