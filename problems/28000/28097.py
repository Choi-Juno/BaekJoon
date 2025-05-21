N = int(input())
study = list(map(int, input().split()))

total = 0

for i in range(N):
    total += study[i]

total += (len(study) - 1) * 8

if total > 24:
    day = total // 24
    hour = total % 24
else:
    day = 0
    hour = total

print(day, hour)
