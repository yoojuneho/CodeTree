x = 0
y = 0

for i in range(10):
    n = int(input())

    if n % 3 == 0:
        x += 1
    if n % 5 == 0:
        y += 1

print(x, y, sep=" ")