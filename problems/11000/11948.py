A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
F = int(input())

science = (A + B + C + D) - min(A, B, C, D)
social = max(E, F)

print(science + social)
