# coding=utf-8
import sys


def fun(goods):
    sum = 0
    for g in goods:
        sum += g
    half = sum // 2
    dp = [0] * (half + 1)
    for g in goods:
        for j in range(half, g - 1, -1):
            dp[j] = max(dp[j], dp[j - g] + g)
    for i in range(half, 0, -1):
        if (sum - 2 * dp[i]) in dp:
            print(sum - 2 * dp[i])


if __name__ == "__main__":
    # T
    T = int(sys.stdin.readline().strip())
    goods_list = []
    for i in range(int(T)):
        # 读取第一行的n
        n = int(sys.stdin.readline().strip())
        line = sys.stdin.readline().strip()
        line = line.split(" ")
        goods = [int(x) for x in line]
        fun(goods)
#
# goods = [1,2,3,6,1]
# res = fun(goods)
# print(res)
