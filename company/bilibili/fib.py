from functools import lru_cache


@lru_cache()
def fun(n):
    if n == 1 or n == 2:
        return 1
    return fun(n - 1) + fun(n - 2)


k = 4
array = [[0] * k for _ in range(k)]
path_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
path_num = 0
m, n = 0, 0
i = k ** 2 - 1
while i >= 0:
    if m < k and n < k and array[m][n] == 0:
        array[m][n] = fun(i+1)
        i -= 1
        path = path_list[path_num]
        m, n = m + path[0], n + path[1]
    else:
        path = path_list[path_num]
        m, n = m - path[0], n - path[1]
        path_num += 1
        path_num %= 4
        path = path_list[path_num]
        m, n = m + path[0], n + path[1]

for a in array:
    for b in a:
        print(b, end=' ')
    print()
