import math

A, B, V = map(int, input().split())

day = 1
climb = 0

day = math.ceil((V - B) / (A - B))

print(day)
