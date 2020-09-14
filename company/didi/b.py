from collections import deque


def fun(n, start, end, start_time):
    visited = [0] * (n + 1)
    d = deque()
    d.append(start)
    while d:
        a = d.popleft()
        next_arr = memo[a]
        for item in next_arr:
            if visited[item[0]] == 0:
                visited[item[0]] = item[1] + visited[a]
                d.append(item[0])
            elif visited[item[0]] > item[1] + visited[a]:
                visited[item[0]] = item[1] + visited[a]

    month = int(start_time.split('.')[0])
    day = int(start_time.split('.')[1].split('/')[0])
    hour = int(start_time.split('.')[1].split('/')[1])
    hour = hour + visited[end]

    if hour >= 24:
        day += hour // 24
        hour %= 24

    if day >= 32 and month in [1, 3, 5, 7, 8, 10, 12]:
        month += day // 32
        day %= 32

    if day >= 31 and month in [2, 4, 6, 9, 11]:
        month += day // 31
        day %= 31

    print('{}.{}/{}'.format(month, day, hour))


line = [int(x) for x in input().split(' ')]
n, m = line[0], line[1]

memo = {}
for i in range(m):
    line = [int(x) for x in input().split(' ')]
    u, v, time = line[0], line[1], line[2]
    if u in memo:
        memo[u].append([v, time])
    else:
        memo[u] = [[v, time]]

    if v in memo:
        memo[v].append([u, time])
    else:
        memo[v] = [[u, time]]

line = input().split(' ')
start, end, start_time = int(line[0]), int(line[1]), line[2]

fun(n, start, end, start_time)
