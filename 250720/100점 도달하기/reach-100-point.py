N = int(input())

while N <= 100:
    if N >= 90:
        print('A', end=" ")
    elif 80 <= N < 90:
        print('B', end=" ")
    elif 70 <= N < 80:
        print('C', end=" ")
    elif 60 <= N < 70:
        print('D', end=" ")
    else:
        print('F', end=" ")
    N += 1