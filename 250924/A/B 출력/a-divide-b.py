A, B = map(int, input().split())

# 몫(정수 부분)
result = str(A // B) + "."

# 나머지
remainder = A % B

# 소수점 21자리 구하기
for _ in range(20):
    remainder *= 10
    result += str(remainder // B)
    remainder %= B

print(result)
