import collections
import unittest
from functools import lru_cache
from typing import List

from cachetools import lru

"""
给出一些不同颜色的盒子，盒子的颜色由数字表示，即不同的数字表示不同的颜色。
你将经过若干轮操作去去掉盒子，直到所有的盒子都去掉为止。每一轮你可以移除具有相同颜色的连续 k 个盒子（k >= 1），这样一轮之后你将得到 k*k 个积分。
当你将所有盒子都去掉之后，求你能获得的最大积分和。

 

示例：

输入：boxes = [1,3,2,2,2,3,4,3,1]
输出：23
解释：
[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----> [1, 3, 3, 4, 3, 1] (3*3=9 分) 
----> [1, 3, 3, 3, 1] (1*1=1 分) 
----> [1, 1] (3*3=9 分) 
----> [] (2*2=4 分)
 

提示：

1 <= boxes.length <= 100
1 <= boxes[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-boxes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class SolutionONe:
    """
    dp(boxes) 表示 boxes的分数
    """

    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)

        def same(arr):
            flag = True
            for a in arr:
                if a != arr[0]:
                    flag = False
                    break
            return flag

        @lru_cache(maxsize=12800)
        def dp(bo):
            if same(bo):
                return len(bo) ** 2
            max_num = len(bo)
            for i in range(len(bo)):
                for j in range(i, len(bo)):
                    if bo[i] == bo[j]:
                        for k in range(i + 1, j):
                            for f in range(k, j):
                                print('\t', end='')
                                print(i, j, k, f, bo, bo[k:f + 1], bo[i:k] + bo[f + 1:j + 1])
                                max_num = max(max_num,
                                              dp(bo[k:f + 1]) + dp(bo[i:k] + bo[f + 1:j + 1]) \
                                              + dp(bo[:i]) \
                                              + dp(bo[j + 1:])
                                              )
            return max_num

        return dp(tuple(boxes))


class Solution:
    def removeBoxesDict(self, boxes: List[int]) -> int:

        def dq(boxes):
            if len(boxes) <= 1:
                dic[boxes] = len(boxes)
                return len(boxes)
            if boxes in dic.keys():
                return dic[boxes]
            index = len(boxes)
            for i in range(len(boxes)):
                if boxes[i] != boxes[0]:
                    index = i
                    break
            dic[boxes] = index * index + dq(boxes[index:])
            for i in range(index + 1, len(boxes)):
                if boxes[i] == boxes[0]:
                    dic[boxes] = max(dic[boxes], dq(boxes[:index] + boxes[i:]) + dq(boxes[index:i]))
            return dic[boxes]

        dic = collections.defaultdict(int)
        dq(tuple(boxes))
        return dic[tuple(boxes)]

    def removeBoxes(self, boxes: List[int]) -> int:

        @lru_cache(maxsize=12800)
        def dq(boxes):
            if len(boxes) <= 1:
                return len(boxes)
            index = len(boxes)
            for i in range(len(boxes)):
                if boxes[i] != boxes[0]:
                    index = i
                    break
            tmp = index * index + dq(boxes[index:])
            for i in range(index + 1, len(boxes)):
                if boxes[i] == boxes[0]:
                    tmp = max(tmp, dq(boxes[:index] + boxes[i:]) + dq(boxes[index:i]))
            return tmp
        return dq(tuple(boxes))


class Test(unittest.TestCase):
    def test_1(self):
        nums = [1, 2, 3]
        answer = 3

        result = Solution().removeBoxes(nums)
        self.assertEqual(answer, result)

    def test_2(self):
        nums = [1, 2, 1]
        answer = 5

        result = Solution().removeBoxes(nums)
        self.assertEqual(answer, result)

    def test_one(self):
        nums = [2, 5, 10, 9, 4, 8, 6, 9, 9, 1]
        answer = 16

        result = Solution().removeBoxes(nums)
        self.assertEqual(answer, result)

    def test_two(self):
        nums = [1, 3, 2, 2, 2, 3, 4, 3, 1]
        answer = 23

        result = Solution().removeBoxes(nums)
        self.assertEqual(answer, result)
