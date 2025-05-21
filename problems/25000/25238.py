a, b = map(int, input().split())

defenceRate = a - (a * (b / 100))

print(0 if defenceRate >= 100 else 1)
