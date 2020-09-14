for i in range(10):
    for j in range(10):
        for k in range(10):
            for f in range(10):
                if 1000 * i + 100 * j + 10 * k + f + 1000 * j + 100 * k + 10 * f + i == 8888:
                    print(i, j, k, f)
