A, B = map(int, input().split())
C, D = map(int, input().split())

comparison1 = A + D
comparison2 = C + B

print(min(comparison1, comparison2))
