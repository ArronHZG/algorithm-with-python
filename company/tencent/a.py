def fun(arr):
    line = []
    for index, a in enumerate(arr):
        line.append((a, index))
    line = sorted(line)
    print(line)
    botten_list = []
    for i in range(1, len(line)):
        if line[i - 1][0] == line[i][0]:
            botten_list.append([line[i - 1], line[i]])
    if len(botten_list) == 0:
        return 0


    large = []
    small = []

    for botten in botten_list:
        for i in range(len(line)):
            if line[i][0] > botten[0][0]:

                if line[i][1] <





arr = [5, 4, 3, 2, 1, 2, 3, 4, 5]
fun(arr)

arr2 = [87, 70, 17, 12, 14, 86, 61, 51, 12, 90, 69, 89, 4, 65]
fun(arr2)
