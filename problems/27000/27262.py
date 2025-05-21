n, k, a, b = map(int, input().split())

stair = (n - 1) * a
elevator = (k - 1) * b + (n - 1) * b

print(elevator, stair)
