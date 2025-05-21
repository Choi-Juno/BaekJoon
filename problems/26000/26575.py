N = int(input())

for _ in range(N):
    d, f, p = map(float, input().split())
    cost = d * f * p
    print(f"${cost:.2f}")
