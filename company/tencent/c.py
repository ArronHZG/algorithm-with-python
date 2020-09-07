def fun(lines):
    def judge(l, k):
        arr1 = lines[l][:]
        arr2 = lines[k][:]
        arr1.sort()
        arr2.sort()
        f = True
        for ii in range(6):
            if arr1[ii] != arr2[ii]:
                f = False
                break
        return f

    arr = []
    for index, line in enumerate(lines):
        line_sum = sum(line)
        arr.append([line_sum, index])
    arr = sorted(arr)

    nums = {}
    for i in range(1, len(arr)):
        if arr[i][0] == arr[i - 1][0]:
            if arr[i][0] in nums:
                nums[arr[i][0]].add(arr[i][1])
                nums[arr[i][0]].add(arr[i - 1][1])
            else:
                nums[arr[i][0]] = set()
                nums[arr[i][0]].add(arr[i][1])
                nums[arr[i][0]].add(arr[i - 1][1])
    for item, val in nums.items():
        val = list(val)
        for i in range(len(val)):
            for j in range(i + 1, len(val)):
                flag = judge(arr[i][1], arr[i - 1][1])
                if flag:
                    print('YES')
                    return
    print('NO')
    return


arr = [
    [1, 2, 3, 4, 5, 6],
    [2, 3, 4, 5, 6, 1]
]

# arr = [
#     [1, 2, 3, 4, 5, 6],
#     [8, 5, 4, 1, 2, 3],
#     [2, 3, 4, 5, 6, 7]
# ]
fun(arr)

# T = int(input())
# for _ in range(T):
#     n = int(input())
#     lines = []
#     for _ in range(n):
#         arr = [int(x) for x in input().split(' ')]
#         lines.append(arr)
#     fun(lines)
