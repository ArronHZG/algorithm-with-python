L_list = {(0, 1): (-1, 0),
          (-1, 0): (0, -1),
          (0, -1): (1, 0),
          (1, 0): (0, 1)}

R_list = {(0, 1): (1, 0),
          (1, 0): (0, -1),
          (0, -1): (-1, 0),
          (-1, 0): (0, 1)}


def fun(n, m, order):
    head = (0, -1)
    local = (0, 0)
    for o in order:
        o = o.split(' ')
        if o[0] == 'L':
            head = L_list[head]
        elif o[0] == 'R':
            head = R_list[head]
        elif o[0] == 'G':
            length = int(o[1])
            # print(length)
            x = local[0] + head[0] * length
            y = local[1] + head[1] * length
            # print(x, y)
            x = max(x, 0)
            y = max(y, 0)
            x = min(x, n - 1)
            y = min(y, n - 1)
            local = (x, y)
        elif o[0] == 'P':
            print(local[0], local[1])


T = int(input().strip())
for i in range(T):
    line = input().strip().split(' ')
    n = int(line[0])
    m = int(line[1])
    order = []
    for _ in range(m):
        order.append(input().strip())
    print("Case #{}:".format(i + 1))
    fun(n, m, order)
