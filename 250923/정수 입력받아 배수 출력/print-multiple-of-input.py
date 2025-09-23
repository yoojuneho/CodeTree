n = int(input())

for i in range(1, (5 * n + 1)):
    if i % n == 0:
        print(i, end=' ')