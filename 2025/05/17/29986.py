N, H = map(int, input().split())

height = list(map(int, input().split()))
count = 0

for i in range(N):
    if height[i] <= H:
        count += 1

print(count)
