lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
lst3 = list(map(int, input().split()))
tmp = input()
lst4 = list(map(int, input().split()))
lst5 = list(map(int, input().split()))
lst6 = list(map(int, input().split()))
lsta = [lst1, lst2, lst3]
lstb = [lst4, lst5, lst6]

for i in range(3):
    for j in range(3):
        print(lsta[i][j] * lstb[i][j], end=" ")
    print()