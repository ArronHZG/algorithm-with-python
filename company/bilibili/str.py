import sys


def fun(A, B):
    dict_A = {}
    for a in A:
        if a not in dict_A:
            dict_A[a] = 1
        else:
            dict_A[a] += 1

    dict_B = {}
    for b in B:
        if b not in dict_B:
            dict_B[b] = 1
        else:
            dict_B[b] += 1

    if len(dict_A) != len(dict_B):
        return 0

    for key, val in dict_A.items():
        if val != dict_B[key]:
            return 0

    return 1

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()
print(fun(A, B))
exit()
