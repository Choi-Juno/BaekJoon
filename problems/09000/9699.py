N = int(input())

for i in range(N):
    a, b, c, d, e = map(int, input().split())

    print(f"Case #{i + 1}: {max(a, b, c, d, e)}")
