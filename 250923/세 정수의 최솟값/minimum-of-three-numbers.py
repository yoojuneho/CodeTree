a, b, c = map(int, input().split())

if a == b and b == c:
    print(a)
elif a == b and a != c:
    if a < c:
        print(a)
    else:
        print(c)
elif a == c and a != b:
    if a < b:
        print(a)
    else:
        print(b)
elif b == c and b != a:
    if b < a:
        print(b)
    else:
        print(a)
elif a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
elif c < a and c < b:
    print(c)