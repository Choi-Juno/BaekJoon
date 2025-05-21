N = int(input())

minTime = 1000000

for i in range(N):
    A, B = map(int, input().split())
    minTime = B if A <= B and B < minTime else minTime

print(minTime if minTime != 1000000 else -1)
