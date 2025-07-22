lst = []
for _ in range(4):
    lst.append(list(map(int, input().split())))

cnt = 0
for i in range(4):
    for j in range(4):
        if lst[i][j] % 5 == 0:
            cnt += 1

print(cnt)