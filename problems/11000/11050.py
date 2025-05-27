import math


def bino_coef(n, k):
    if n == k or k == 0:
        return 1
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


N, K = map(int, input().split())

print(bino_coef(N, K))
