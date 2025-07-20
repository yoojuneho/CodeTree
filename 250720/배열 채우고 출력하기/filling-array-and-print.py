'''
arr = list(map(str, input().split()))

for i in range(len(arr)):
    print(arr[9-i], end="")
'''

arr = list(map(str, input().split()))

arr.reverse()

for i in range(len(arr)):
    print(arr[i], end="")