A, B = map(int, input().split())

M = (B - A) / 400

print(f"{1 / (1 + 10 ** M):.8f}")
