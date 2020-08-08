import unittest
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return [-1, - 1]

        left = 0
        right = len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum < target:
                left += 1
            elif sum > target:
                right -= 1

        return [-1, - 1]


class Test(unittest.TestCase):
    def test_one(self):
        input = [2, 7, 11, 15]
        target = 9
        answer = [1, 2]

        result = Solution().twoSum(input, target)
        self.assertEqual(result, answer)
