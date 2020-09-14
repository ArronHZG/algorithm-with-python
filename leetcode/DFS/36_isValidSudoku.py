import unittest
from typing import List


def show(board):
    for line in board:
        print(line)

    print('-' * 20)


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_arr = [[0] * 9 for _ in range(9)]
        col_arr = [[0] * 9 for _ in range(9)]
        space_arr = [[0] * 9 for _ in range(9)]
        for row in range(9):
            for col in range(0, 9):
                if board[row][col] != '.':
                    num = int(board[row][col])
                    row_arr[row][num - 1] += 1
                    col_arr[col][num - 1] += 1
                    space_arr[row // 3 * 3 + col // 3][num - 1] += 1
                    if row_arr[row][num - 1] >= 2 or \
                            col_arr[col][num - 1] >= 2 or \
                            space_arr[row // 3 * 3 + col // 3][num - 1] >= 2:
                        return False
        return True


class Test(unittest.TestCase):
    def test_one(self):
        nums = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]

        answer = True

        result = Solution().isValidSudoku(nums)
        self.assertEqual(answer, result)
