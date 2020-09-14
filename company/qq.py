from collections import OrderedDict

# line = [int(x) for x in input().strip().split(' ')]
# n, m = line[0], line[1]
#
# arr = []
# for i in range(m):
#     arr.append([int(x) for x in input().strip().split(' ')])

n, m = 3, 2
arr = [[1, 1], [2, 0]]
print(arr)

# 记录小于个数, 首位不相同, 在记录上的人都不是A

id = OrderedDict()

for i in range(1, n + 1):
    id[i] = 1

for i in range(len(arr)):
    id[arr[i][0]] = 0

for key, val in id.items():
    if val == 1:
        print(key)
