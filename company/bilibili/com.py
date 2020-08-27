import sys


def fun(M, max_times):
    n = len(M)
    dp = [[0] * (max_times + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        w = M[i - 1][0]
        v = M[i - 1][1]
        for j in range(1, max_times + 1):
            if w > j:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
    return dp[-1][-1]


line = sys.stdin.readline().strip()

in_line = line.split(' ')
n = int(in_line[0])
max_times = int(in_line[1])
M = []
for i in range(n):
    line = sys.stdin.readline().strip()
    in_line = line.split(' ')
    M.append([int(x) for x in in_line])

print(fun(M, max_times))
