import math


def fun_3(a, b, c, d, x):
    return a * x ** 3 + b * x ** 2 + c * x + d


def det_fun_3(a, b, c, x):
    return 3 * a * x ** 2 + 2 * b * x + c


def newton(x0, a, b, c, d, e=1e-8):
    p0 = x0 * 1.0
    for i in range(50):
        print(p0)
        p = p0 - fun_3(a, b, c, d, p0) / det_fun_3(a, b, c, p0)
        if abs(p - p0) < e:
            return p
        else:
            p0 = p


def fun(n, arr):
    if n == 1:
        return [-arr[0] / arr[1]]

    if n == 2:
        # ax2+bx+c=0
        a = arr[2]
        b = arr[1]
        c = arr[0]
        det = b * b - 4 * a * c
        if det < 0:
            return []
        d = math.sqrt(det)
        x1 = (-b + d) / (2 * a)
        x2 = (-b - d) / (2 * a)
        if x1 == x2:
            return [x1]
        else:
            return sorted([x1, x2])

    if n == 3:
        a = arr[3]
        b = arr[2]
        c = arr[1]
        d = arr[0]
        i = newton(0.00000001, a=a, b=b, c=c, d=d)
        print(i)


arr = [1, 2, 1]
re = fun(2, arr)

arr = [1, 4, 2, 5]
re = fun(3, arr)

if re:
    for r in re:
        print("{:.2f}".format(r))
else:
    print('No')
