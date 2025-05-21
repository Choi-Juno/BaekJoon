A, B, C = map(int, input().split())

if A == C:
    print("S")
elif A == B:
    print("S")
elif B == C:
    print("S")
elif A + B == C:
    print("S")
elif A + C == B:
    print("S")
elif B + C == A:
    print("S")
else:
    print("N")
