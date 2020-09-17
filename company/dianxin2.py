import math
from collections import OrderedDict

s = input()

d = OrderedDict()
min_time = math.inf
for c in s:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1

for key, val in d.items():
    min_time = min(min_time, val)

res = []
for key, val in d.items():
    if val == min_time:
        res.append(key)

for c in s:
    if c not in res:
        print(c, end='')
print()
