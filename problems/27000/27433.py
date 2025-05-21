N = int(input())
N_factorial = 1

for i in range(1, N + 1):
    if N == 0:
        N_factorial = 1
        break
    N_factorial *= i

print(N_factorial)
