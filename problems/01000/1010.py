import math

T = int(input())

result = 1

for _ in range(T):
    N, M = map(int, input().split())
    result = math.comb(M, N)
    print(result)
