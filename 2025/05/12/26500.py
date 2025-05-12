N = int(input())

for _ in range(N):
    a, b = map(float, input().split())
    print(f"{abs(min(a, b) - max(a, b)):.1f}")
