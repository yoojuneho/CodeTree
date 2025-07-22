start, end = map(int, input().split())
x = 0

# Please write your code here.
for i in range(start, end+1):
    tmp = 0
    for j in range(1, i+1):
        if i % j == 0:
            tmp += 1
    if tmp == 3:
        x += 1

print(x)