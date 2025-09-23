def classify(symptom, temp):
    temp = int(temp)
    if symptom == 'Y' and temp >= 37:
        return 'A'
    elif symptom == 'N' and temp >= 37:
        return 'B'
    elif symptom == 'Y' and temp < 37:
        return 'C'
    else:
        return 'D'

xa, xb = input().split()
ya, yb = input().split()
za, zb = input().split()

cases = [classify(xa, xb), classify(ya, yb), classify(za, zb)]

# A가 2명 이상이면 위급
if cases.count('A') >= 2:
    print('E')
else:
    print('N')
