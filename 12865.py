n, k = map(int, input().split())

thing = [[0, 0]]
dp = [[0] * (k + 1) for _ in range(n + 1)]

for _ in range(n):
    thing.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(i, k + 1):
        weight = thing[i][0]
        value = thing[i][1]

        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[n][k])
