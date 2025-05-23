N = int(input())
str = input()

result = 0

for i in range(N):
    result += (ord(str[i]) - 96) * (31**i)

print(result % 1234567891)
