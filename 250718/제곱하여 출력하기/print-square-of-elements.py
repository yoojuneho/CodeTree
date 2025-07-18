N = int(input())
arr = list(map(int, input().split()))

#for i in arr:
#    print(i**2, end=" ")

for i in range(N):
    print(arr[i]**2, end=" ")