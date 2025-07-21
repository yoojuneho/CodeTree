N = int(input())

while True:
    if N > 25:
        print("Lower")
        N = int(input())
    elif N < 25:
        print("Higher")
        N = int(input())
    else:
        print("Good")
        break