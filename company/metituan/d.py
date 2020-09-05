def fun(n, m, arr):
    times = 0
    for l in range(1, m + 1):
        for r in range(l, m + 1):
            tt = []
            for a in arr:
                if a < l or a > r:
                    tt.append(a)
            if len(tt) <= 1:
                times += 1
            else:
                flag = True
                for index in range(1, len(tt)):
                    if tt[index] < tt[index - 1]:
                        flag = False
                        break
                if flag:
                    times += 1
    print(times)


n, m = 5, 5
arr = [4, 1, 4, 1, 2]

fun(n, m, arr)
