arr = [0, 3, 1, 2]


def func(K, N, arr):
    for i in range(N):
        # find max swappable val in range[i+1, i+K]
        imax = i
        for j in range(i + 1, min(N, i + K + 1)):
            if arr[imax] < arr[j]:
                imax = j

        K -= imax - i  # update K val
        # psuedo swap
        val = arr.pop(imax)
        arr.insert(i, val)


        if K == 0:
            break  # stop when K == 0

    # K is too large that arr is already sorted after N iteration.
    # if K is even then arr keeps the same, because remaining swaps can be reduced
    # if K is odd, then swap the last two elements to keep arr max
    if K != 0 and K % 2 == 1:
        arr[-1], arr[-2] = arr[-2], arr[-1]

    return arr


print(func(2, 4, arr))
