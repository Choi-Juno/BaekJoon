STR, DEX, INT, LUK, N = map(int, input().split())

statSum = STR + DEX + INT + LUK

statDiff = (4 * N - statSum) if (4 * N - statSum) > 0 else 0

print(statDiff)
