N = int(input())
minStation = [float("inf"), float("inf")]
for _ in range(N):
    x, y = map(int, input().split())
    minStation = [x, y] if y < minStation[1] else minStation

print(*minStation)
