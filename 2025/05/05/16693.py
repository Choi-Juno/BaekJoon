import math

A1, P1 = map(int, input().split())
R1, P2 = map(int, input().split())

if P1 / A1 < P2 / (R1 * R1 * math.pi):
    print("Slice of pizza")
else:
    print("Whole pizza")
