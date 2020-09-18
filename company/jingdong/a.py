def fun(n, p):
    dp = [0] * (p + 1)

    for _ in range(n):
        goods = [int(x) for x in input().split()]
        for i in range(goods[0]):
            for j in range(p, goods[1] - 1, -1):
                dp[j] = max(dp[j - 1], dp[j - goods[1]] + goods[2])
    print(dp[-1])


line = [int(x) for x in input().split()]
n = line[0]
p = line[1]
fun(n, p)
