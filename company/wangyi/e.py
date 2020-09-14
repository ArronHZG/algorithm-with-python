def argmin(peo_num, memo):
    min_length = 10000
    index = -1
    for i in range(peo_num):
        if min_length > len(memo[i]) > 0:
            index = i
            min_length = len(memo[i])
    return index


man = [int(x) for x in input().split(' ')]
woman = [int(x) for x in input().split(' ')]
peo_num = max(max(man), max(woman)) + 1
memo = [[] for _ in range(peo_num)]
n = int(input())
for i in range(n):
    line = [int(x) for x in input().split(' ')]
    print(line)
    memo[line[0]].append(line[1])
    memo[line[1]].append(line[0])
print(memo)

match_num = 0

while True:
    index = argmin(peo_num, memo)
    if index == -1:
        break
    for i in memo[index]:
        min_length = 100000
        match_id = -1
        if min_length > len(memo[i]):
            min_length = len(memo[i])
            match_id = i

    if match_id != -1:
        match_num += 1
        memo[index] = []
        memo[match_id] = []
        for i in range(peo_num):
            if index in memo[i]:
                memo[i].remove(index)
            if match_id in memo[i]:
                memo[i].remove(match_id)
    else:
        break


print(match_num)
