# coding=utf-8
import datetime
import sys


def fun(a_list, b_list):
    dp = [0] * (len(a_list))
    dp[0] = a_list[0]
    for i in range(1, len(dp)):
        dp[i] = min(dp[i - 1] + a_list[i], dp[i - 2] + b_list[i - 1])
    strTime = '08:00:00'
    startTime = datetime.datetime.strptime(strTime, "%H:%M:%S")
    print((startTime + datetime.timedelta(seconds=dp[-1])).strftime("%H:%M:%S"))


# a_list = [5, 4, 3, 4, 5]
# b_list = [10, 5, 8, 5]
# fun(a_list, b_list)


if __name__ == "__main__":
    # T
    T = int(sys.stdin.readline().strip())
    for i in range(int(T)):
        # 读取第一行的n
        n = int(sys.stdin.readline().strip())
        line = sys.stdin.readline().strip()
        line = line.split(" ")
        a_list = [int(x) for x in line]
        line = sys.stdin.readline().strip()
        line = line.split(" ")
        b_list = [int(x) for x in line]
        fun(a_list, b_list)
