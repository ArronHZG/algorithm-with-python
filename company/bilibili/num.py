import sys


def num(n):
    nums = [0] * (n + 1)
    nums[0] = 1
    nums[1] = 1
    for i in range(2, n + 1):
        if nums[i] == 0:
            for j in range(i + i, n + 1, i):
                nums[j] = 1
    bias = []
    for i in range(n + 1):
        if nums[i] == 0:
            bias.append(i)
    count = 0
    for i in range(len(bias)):
        for j in range(i, len(bias)):
            s = sum(bias[i:j])
            if s == n:
                count += 1
    if bias[-1] == n:
        count += 1
    return count


a = num(41)
print(a)
# line = sys.stdin.readline().strip()
# a = int(line)
# print(num(a))
