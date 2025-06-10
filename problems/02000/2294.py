n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [float("inf")] * (k + 1)
dp[0] = 0

for coin in coins:
    for i in range(coin, k + 1):
        if dp[i - coin] != float("inf"):
            dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[k] if dp[k] != float("inf") else -1)
