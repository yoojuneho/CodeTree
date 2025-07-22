N = int(input())

tmp = []
lst = []
cnt = 1
sign = 1

for _ in range(N):
    tmp.append(cnt)
    cnt += 1

rtmp = tmp[::-1]

lst = []

for _ in range(N):
    if sign == 1:
        lst.append(tmp)
        sign = 0
    elif sign == 0:
        lst.append(rtmp)
        sign = 1

for i in range(4):
    for j in range(4):
        print(lst[i][j], end="")
    print()