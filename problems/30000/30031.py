N = int(input())

total = 0

for _ in range(N):
    w, h = map(int, input().split())
    if w == 136:
        total += 1000
    elif w == 142:
        total += 5000
    elif w == 148:
        total += 10000
    else:
        total += 50000

print(total)
