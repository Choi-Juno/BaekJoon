N = int(input())

factorial = 1

for i in range(1, N + 1):
    factorial *= i

factorial = str(factorial)
print(factorial[-1])
