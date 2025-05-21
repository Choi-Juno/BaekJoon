n, m, k, a, b, c = map(int, input().split())

max_army = max(n * a, m * b, k * c)
king = []

if max_army == n * a:
    king.append("Joffrey")
if max_army == m * b:
    king.append("Robb")
if max_army == k * c:
    king.append("Stannis")

print(*king)
