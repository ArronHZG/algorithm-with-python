def ifValid(nums):
    nums = sorted(nums)
    num_zero = 0
    for a in nums:
        if a == 0:
            num_zero += 1
        else:
            break
    nums = nums[num_zero:]

    k = 0
    for i in range(len(nums)):
        if nums[i] == i + nums[0] + k:
            pass
        if nums[i] < i + nums[0] + k:
            print('Invalid')
            return
        if nums[i] > i + nums[0] + k:
            k += nums[i] - (i + nums[0] + k)
            if num_zero < k:
                print('Invalid')
                return
    print('Valid')


ifValid([0, 1, 2, 3])
ifValid([0, 1, 0, 3])
ifValid([0, 1, 0, 1])
ifValid([1, 2, 3, 6, 7, 8, 0, 0])

# while True:
#     n = input()
#     ll = [int(x) for x in input().strip().split(' ')]
#     ifValid(ll)
