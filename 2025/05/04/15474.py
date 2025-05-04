N, A, B, C, D = map(int, input().split())

if N % A != 0:
    charge_A = (N // A + 1) * B
else:
    charge_A = N // A * B

if N % C != 0:
    charge_C = (N // C + 1) * D
else:
    charge_C = N // C * D

print(min(charge_A, charge_C))
