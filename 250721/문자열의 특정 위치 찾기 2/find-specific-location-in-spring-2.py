N = input()

fruits = ["apple", "banana", "grape", "blueberry", "orange"]
cnt = 0

for i in range(5):
    if N in fruits[i][2:4]:
        print(fruits[i])
        cnt += 1

print(cnt)