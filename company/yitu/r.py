MOD = 100000007


def fun(array):
    for i in range(len(array)):
        array[i] **= 2
    sum = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[j] > array[i]:
                for k in range(j + 1, len(array)):
                    if array[i] < array[k] < array[j]:
                        sum += 1
                        sum %= MOD
    print(sum)


array = [-3, 5, 2, 4, -1]
fun(array)
