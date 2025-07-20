N = int(input())

lst = list(map(int, input().split()))
new_l = []

for i in range(N):
    if lst[i] % 2 == 0:
        new_l.append(lst[i])

new_l.reverse()

for i in new_l:
    print(i, end=" ")