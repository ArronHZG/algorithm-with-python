def find_start(string, n):
    for i in range(n):
        if string[i] == 'M':
            for j in range(i + 1, n):
                if string[j] == 'T':
                    return j + 1


def find_end(string, n):
    for i in range(n - 1, -1, -1):
        if string[i] == 'T':
            for j in range(i - 1, -1, -1):
                if string[j] == 'M':
                    return j


def fun(string):
    n = len(string)
    begin = find_start(string, n)
    end = find_end(string, n)
    print(string[begin:end])


s = 'MMATSATMMT'
fun(s)
