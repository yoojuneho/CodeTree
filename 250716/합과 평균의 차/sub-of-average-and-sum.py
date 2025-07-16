a, b, c = map(int, input().split())

sum = a + b + c
avg = int(sum / 3)
sub = sum - avg

print(sum, avg, sub, sep='\n')