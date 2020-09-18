import unittest
import random
from typing import List

from utils.timer import timer

import sys

sys.setrecursionlimit(1000000000)


class Solution:
    @timer
    def quickSort(self, arr):
        """
            最好的情况是O(n)，最差的情况是O(n2)，所以平时说的O(nlogn)

            最差情况, 每次都选择最大或者最小的数, 退化成 冒泡排序

            区间一致性 [i,j) 左开右闭
        """

        def quick(low, high):
            if low + 1 >= high:
                return
            anchor = arr[low]
            separate = low
            for i in range(low + 1, high):
                if arr[i] < anchor:
                    separate += 1
                    arr[i], arr[separate] = arr[separate], arr[i]
            arr[low], arr[separate] = arr[separate], arr[low]
            quick(low, separate)
            quick(separate + 1, high)

        quick(0, len(arr))

    @timer
    def randomQuickSort(self, arr):
        """

        随机选择一个数进行比较
        """

        def quick(low, high):
            if low + 1 >= high:
                return

            # 随机选择一个数, 和首个数互换
            rand = random.randint(low, high - 1)
            arr[low], arr[rand] = arr[rand], arr[low]

            # 然后后续过程与正常的快拍一致
            anchor = arr[low]
            separate = low
            for i in range(low + 1, high):
                if arr[i] < anchor:
                    separate += 1
                    arr[i], arr[separate] = arr[separate], arr[i]
            arr[low], arr[separate] = arr[separate], arr[low]
            quick(low, separate)
            quick(separate + 1, high)

        quick(0, len(arr))

    @timer
    def mergeSort(self, nums):
        def merge(low, high):
            if low + 1 >= high:
                return
            mid = (high - low) // 2 + low
            merge(low, mid)
            merge(mid, high)

            # 开始归并
            tmp = []
            i, j = low, mid
            while i < mid and j < high:
                if nums[i] < nums[j]:
                    tmp.append(nums[i])
                    i += 1
                else:
                    tmp.append(nums[j])
                    j += 1
            if i == mid:
                while j < high:
                    tmp.append(nums[j])
                    j += 1
            if j == high:
                while i < mid:
                    tmp.append(nums[i])
                    i += 1

            nums[low: high] = tmp

        merge(0, len(nums))


class Test(unittest.TestCase):
    def test_one(self):
        nums = [72, 6, 57, 88, 60, 42, 83, 73, 48, 85]
        answer = [6, 42, 48, 57, 60, 72, 73, 83, 85, 88]

        Solution().quickSort(nums)
        self.assertEqual(nums, answer)

    def test_two(self):
        nums = [7, 6, 5, 4, 3, 2, 1]
        answer = [1, 2, 3, 4, 5, 6, 7]

        Solution().randomQuickSort(nums)
        self.assertEqual(nums, answer)

    def test_time(self):
        nums = [x for x in range(10000, -1, -1)]

        Solution().quickSort(nums)

        nums = [x for x in range(10000, -1, -1)]

        Solution().randomQuickSort(nums)

        # quickSort：4.9361 s
        # randomQuickSort：0.0264 s

    def test_merge_one(self):
        nums = [7, 6, 5, 4, 3, 2, 1]
        answer = [1, 2, 3, 4, 5, 6, 7]

        Solution().mergeSort(nums)
        self.assertEqual(nums, answer)

    def test_merge_time(self):
        nums = [x for x in range(10000, -1, -1)]

        Solution().randomQuickSort(nums)

        nums = [x for x in range(10000, -1, -1)]

        Solution().mergeSort(nums)

        # randomQuickSort：0.0306 s
        # mergeSort：0.0248 s
