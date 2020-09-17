import math


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, x):
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        print(self.stack[-1])
        return self.stack[-1]

    def getMin(self):
        print(self.min_stack[-1])
        return self.min_stack[-1]


miniStack = MinStack()
n = int(input())
for i in range(n):
    line = input().split()
    if len(line) == 2:
        miniStack.push(int(line[1]))
    elif line[0] == 'top':
        miniStack.top()
    elif line[0] == 'pop':
        miniStack.pop()
    elif line[0] == 'getMin':
        miniStack.getMin()
