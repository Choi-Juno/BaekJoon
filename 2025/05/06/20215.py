W, H = map(int, input().split())

area = W + H

res = area - (W**2 + H**2) ** 0.5

print(res)
