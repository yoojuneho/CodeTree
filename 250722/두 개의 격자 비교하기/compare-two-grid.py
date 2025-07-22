row, col = map(int, input().split())

lst1 = [list(map(int, input().split())) for _ in range(row)]

lst2 = [list(map(int, input().split())) for _ in range(row)]

for i in range(row):
    for j in range(col):
        print(0 if lst1[i][j] == lst2[i][j] else 1, end=" ")
    print()