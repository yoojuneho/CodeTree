N = int(input())
lst = []

for i in range(1,N+1):
    cnt = 0
    tmp = []
    for j in range(N):
        if cnt == 0:
            tmp.append(i)
            cnt = 1
        elif cnt == 1:
            tmp.append(N + 1 - i)
            cnt = 0
    lst.append(tmp)

for i in range(N):
    for j in range(N):
        print(lst[i][j], end="")
    print()