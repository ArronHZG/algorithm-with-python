from copy import deepcopy


def show(dp):
    for i in range(len(dp)):
        print(dp[i])


def count(s):
    n = len(s)
    dp = [[{'a': 0,
            'b': 0,
            'c': 0,
            'x': 0,
            'y': 0,
            'z': 0} for _ in range(n)] for _ in range(n)]

    show(dp)
    for i in range(n):
        if s[i] in dp[i][i]:
            dp[i][i][s[i]] = 1
    print()

    show(dp)

    for i in range(n):
        for j in range(i + 1, n):
            dp[i][j] = deepcopy(dp[i][j - 1])
            if s[j] in dp[i][j]:
                dp[i][j][s[j]] += 1

    print()

    show(dp)

    length = 0
    for i in range(n):
        for j in range(i, n):
            flag = True
            for key, val in dp[i][j].items():
                if val % 2 != 0:
                    flag = False

            if flag:
                length = max(length, j - i + 1)

    return length


print(count('amabc'))
