# coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys


def fun(n, str_list):
    memory = {}

    for s in str_list:
        if s in memory:
            memory[s] += 1
        else:
            memory[s] = 1
    result = 0
    for key, value in memory.items():
        if value / n >= 0.01:
            result += 1
    return result


if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    str_list = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        str_list.append(line)
    re = fun(n, str_list)
    print(re)

# n = 5
#
# str_list = ['1', '2', '3', '4', '4']
# re = fun(n, str_list)
# print(re)
