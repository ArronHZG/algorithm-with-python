def fun(s):
    arr = [0] * 5

    # 0 数字
    # 1 大写
    # 2 小写
    # 3 特殊
    # 4 长度 大于 8

    s = list(s)

    if len(s) >= 8:
        arr[4] = 1

    for i in range(len(s)):
        if s[i].islower():
            arr[2] = 1
        if s[i].isupper():
            arr[1] = 1
        if s[i].isdigit():
            arr[0] = 1
        if (not s[i].islower()) and (not s[i].isupper()) and (not s[i].isdigit()):
            arr[3] = 1
    print(arr)
    if sum(arr) == 5:
        print('Ok')
        return True
    else:
        print('Irregular password')
        return False


# while True:
#     s = input().strip()
#     fun(s)

s = '12_Aaqq12'
fun(s)