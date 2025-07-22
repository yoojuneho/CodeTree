lst = []

for _ in range(4):
    lst.append(list(map(int, input().split())))

for i in range(4):
    total = sum(lst[i])
    print(total)