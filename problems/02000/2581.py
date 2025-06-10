N = int(input())
M = int(input())

primes = []

for num in range(N, M + 1):
    if num == 1:
        continue
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)

if len(primes) == 0:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))
