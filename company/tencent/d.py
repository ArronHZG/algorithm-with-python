# arr = [int(x) for x in input().split(' ')]
# L = arr[0]
# d = arr[1]
import random

L = 2.0

d = 1.0

sum = 0
for i in range(10000000):
    times = 0
    L = 2
    d = 1
    while L > d:
        times += 1
        L = L - random.uniform(0, L)
    sum += times
print('{:.4f}'.format(sum / 10000000))
