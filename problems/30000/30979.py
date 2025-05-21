T = int(input())
N = int(input())
F = list(map(int, input().split()))

total = sum(F)

print("Padaeng_i Happy" if total >= T else "Padaeng_i Cry")
