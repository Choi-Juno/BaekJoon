N, W, H, L = map(int, input().split())

cows = (W // L) * (H // L)

print(min(cows, N))
