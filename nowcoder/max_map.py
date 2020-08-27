import sys
import unittest
from collections import defaultdict


def max_map(str_list):
    map1 = defaultdict(int)
    map2 = defaultdict(int)
    for s in str_list:
        for index, c in enumerate(s):
            map1[c] += 10 ** (len(s) - index - 1)
    l = sorted(map1.items(), key=lambda item: item[1])

    # 前导为0判断
    if len(l) == 10:
        not_zero_char = []
        for s in str_list:
            not_zero_char.append(s[0])
        i = 0
        while l[i][0] in not_zero_char:
            i += 1
        map2[l[i][0]] = 0
        l.remove(l[i])

    for i in range(10 - len(l), 10, 1):
        map2[l[i - 10 + len(l)][0]] = i
    max_num = 0
    for key, val in map1.items():
        max_num += map1[key] * map2[key]
    return max_num


# class Test(unittest.TestCase):
#     def test_one(self):
#         nums = ['ABC', 'BCA']
#         answer = 1875
#
#         result = max_map(nums)
#         self.assertEqual(answer, result)

if __name__ == "__main__":
    # T
    str_list = []
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        line = sys.stdin.readline().strip()
        str_list.append(line)
    print(max_map(str_list))
