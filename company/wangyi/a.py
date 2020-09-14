line = [int(x) for x in input().split(' ')]

m = line[0]
n = line[1]
tree = dict()

for i in range(n):
    line = input().split(' ')
    if line[0] not in tree:
        tree[line[0]] = []
    tree[line[0]].append(line[2])

print(tree)

num = 0
for key, val in tree.items():
    if len(val) == 2:
        if val[0] not in tree and val[1] not in tree:
            num += 1

print(num)