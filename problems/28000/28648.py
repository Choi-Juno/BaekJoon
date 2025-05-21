n = int(input())

duration = 99999

for _ in range(n):
    ti, li = map(int, input().split())
    if ti + li < duration:
        duration = ti + li

print(duration)
