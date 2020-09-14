def fun(n, k, arr):
    s = set()
    while True:
        len_s = len(s)
        for line in arr:
            if line[2] <= k:
                if len(s) == 0 or line[0] in s or line[1] in s:
                    s.add(line[0])
                    s.add(line[1])
        if len_s == len(s):
            break

    if len(s) == n:
        print('Yes')
    else:
        print('No')


T = int(input())

for i in range(T):
    line = [int(x) for x in input().split(' ')]
    n, m, k = line[0], line[1], line[2]
    arr = []
    for i in range(m):
        line = [int(x) for x in input().split(' ')]
        arr.append(line)
    fun(n, k, arr)
