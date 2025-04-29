N = int(input())

sum1 = 0
sum2 = 0
sum3 = 0

for i in range(1, N + 1):
    sum1 += i
    sum3 += i**3

sum2 = sum1**2

print(sum1)
print(sum2)
print(sum3)
