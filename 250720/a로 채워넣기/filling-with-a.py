N = input()

lst = list(N)
lst[1] = 'a'
lst[-2] = 'a'
print(''.join(lst))