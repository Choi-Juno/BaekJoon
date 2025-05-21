A, B, C = map(int, input().split())

if A == B == C:
    print(0)
else:
    print(max(A, B, C) * 3 - sum([A, B, C]))
