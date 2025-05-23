A, B = map(int, input().split())

GCD = 0  # Greatest Common Divisor
GCM = 0  # Greatest Common Multiple

for i in range(1, min(A, B) + 1):
    if A % i == 0 and B % i == 0:
        GCD = i

GCM = (A // GCD) * (B // GCD) * GCD

print(GCD)
print(GCM)
