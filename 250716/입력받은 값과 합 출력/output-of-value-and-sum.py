a, b = map(int, input().split())

while not (1 <= a <= 100 and 1 <= b <= 100):
    a, b = map(int, input().split())

print(a, b, a+b)