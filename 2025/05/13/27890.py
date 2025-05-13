import math

x0, N = map(int, input().split())

for _ in range(N):
    if x0 % 2 == 0:
        x0 = math.floor(x0 / 2) ^ 6
    else:
        x0 = x0 * 2 ^ 6

print(x0)
