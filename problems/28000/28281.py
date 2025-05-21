N, X = map(int, input().split())
prices = []

price = list(map(int, input().split()))

for i in range(N - 1):
    prices.append((price[i] + price[i + 1]) * X)

print(min(prices))
