def func(N, H, arr):
    stack = []
    res = [0] * (1 + N)
    for i in range(N):
        arr[i] = (arr[i] - H) / (i + 1)
        while stack != [] and arr[i] > arr[stack[-1]]:
            stack.pop()
        res[i + 1] = 0 if stack == [] else stack[-1] + 1
        stack.append(i)
    for a in res[1:]:
        print(a)

N = 9
H = 5
arr = [5, 4, 3, 4, 3, 3, 3, 3, 3]
func(N, H, arr)
