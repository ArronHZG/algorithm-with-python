from collections import defaultdict


def fun(string):
    d = {}
    start = 0
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            if i + 2 == len(string):
                if string[i] in d.keys():
                    d[string[i]].append((start, i + 1))
                else:
                    d[string[i]] = [(start, i + 1)]
        else:
            if string[i] in d.keys():
                d[string[i]].append((start, i))
            else:
                d[string[i]] = [(start, i)]
            start = i + 1
    if start == len(string) - 1:
        if string[start] in d.keys():
            d[string[start]].append((start, start))
        else:
            d[string[start]] = [(start, start)]
    max_len = 0
    for key, val in d.items():
        for i in range(len(val) - 1):
            max_len = max(val[i][1] - val[i][0] + 2, max_len)
            if val[i][1] + 2 == val[i + 1][0]:
                max_len = max(val[i + 1][1] - val[i][0] + 1, max_len)
        max_len = max(val[-1][1] - val[-1][0] + 2, max_len)
        # print(max_len, val)
    print(min(max_len, len(string)))


fun('123112111')
fun('111')
