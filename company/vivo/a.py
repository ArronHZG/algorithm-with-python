def isHui(s):
    n = len(s)
    i, j = 0, n - 1
    while i <= j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


def fun(s):
    n = len(s)
    i, j = 0, n - 1
    index = -1
    while i <= j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            index = -2
            if isHui(s[i: j]):
                index = j
            if isHui(s[i + 1:j + 1]):
                index = i
            break

    return index


s = input()
s = list(s)
index = fun(s)

if index == -1:
    print(''.join(s))
elif index == -2:
    print('false')
else:
    print(''.join(s[:index] + s[index + 1:]))
