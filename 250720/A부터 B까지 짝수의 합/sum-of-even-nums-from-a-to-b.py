A, B = map(int, input().split())
x = 0

for i in range(A, B+1):
    if i % 2 == 0:
        x += i

print(x)