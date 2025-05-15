n, m = map(int, input().split())

ans = 0

for _ in range(n):
    str = input()
    if "+" in str:
        ans += 1

print(ans)
