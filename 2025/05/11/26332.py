N = int(input())

for _ in range(N):
    a, b = map(int, input().split())

    if a == 1:
        print(a, b)
        print(b)
    elif a >= 2:
        print(a, b)
        print((a - 1) * (b - 2) + b)
