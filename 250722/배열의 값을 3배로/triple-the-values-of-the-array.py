lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
lst3 = list(map(int, input().split()))

lst = [lst1, lst2, lst3]

for i in range(3):
    for j in range(3):
        print(lst[i][j] * 3, end=" ")
    print()