g = int(input())
age = int(input())

if g == 0:
    if age > 18:
        print("MAN")
    else:
        print("BOY")
elif g == 1:
    if age > 18:
        print("WOMAN")
    else:
        print("GIRL")