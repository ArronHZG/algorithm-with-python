class CtrlCV:
    def __init__(self, a, n):
        self.a = a
        self.b = [-1] * n

    def copy(self, k, x, y):
        self.b[y:y + k] = self.a[x:x + k]

    def select(self, i):
        print(self.b[i])


n = int(input().strip())
a = [int(x) for x in input().strip().split(' ')]
ctrl = CtrlCV(a, n)
m = int(input().strip())
for _ in range(m):
    line = [int(x) for x in input().strip().split(' ')]
    if line[0] == 1:
        ctrl.copy(line[1], line[2] - 1, line[3] - 1)
    elif line[0] == 2:
        ctrl.select(line[1] - 1)
