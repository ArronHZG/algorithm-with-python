# str_1 = 'pony'
# str_2 = 'pponyy'


def fun(str1, str2):
    num = 0
    for i in range(len(str2)):
        for j in range(i + 1, len(str2) + 1):
            if str2[i:j] in str1:
                num += 1
    return num


if __name__ == '__main__':
    # n, m = list(map(int, input().split()))
    # str1 = input()
    # str2 = input()
    str1 = 'buqcljjivs'
    str2 = 'nwlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmcoqhnwnkuewhsqmgb'
    print(fun(str1, str2))
