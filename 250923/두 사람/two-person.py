Aa, As = input().split()
Ba, Bs = input().split()

Aa, Ba = int(Aa), int(Ba)

if (Aa >= 19 and As == 'M') or (Ba >= 19 and Bs == 'M'):
    print(1)
else:
    print(0)