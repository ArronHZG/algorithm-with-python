def fun(n, arr):
    ret = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] not in ret:
                ret.append(arr[i][j])
                break
    for r in ret:
        print(r, end=' ')
    print()


n = int(input().strip())
arr = []
for i in range(n):
    tmp = [int(x) for x in input().strip().split(' ')]
    arr.append(tmp)
fun(n, arr)

# arr = [[1, 5, 3, 4, 2],
#        [2, 3, 5, 4, 1],
#        [5, 4, 1, 2, 3],
#        [1, 2, 5, 4, 3],
#        [1, 4, 5, 2, 3]]
# fun(5, arr)
