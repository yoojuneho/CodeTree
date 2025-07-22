lst = []
for _ in range(4):
    lst.append(list(map(int, input().split())))

total = 0

for i in range(4):
    for j in range(4):
        if i < j:
            continue
        total += lst[i][j]

print(total)