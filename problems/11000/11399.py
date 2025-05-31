N = int(input())

time = list(map(int, input().split()))
time.sort()

duration = 0
result = 0

for i in range(N):
    duration += time[i]
    result += duration

print(result)
