N = input()

New_N = N.replace(N[1], 'a')
New_N = N.replace(N[-2], 'a')

print(New_N)