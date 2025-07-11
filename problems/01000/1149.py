N = int(input())

dp = [[0] * 3 for _ in range(N)]
cost = []

for i in range(N):
    R, G, B = map(int, input().split())
    cost.append([R, G, B])

dp[0][0], dp[0][1], dp[0][2] = cost[0][0], cost[0][1], cost[0][2]

for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]

print(min(dp[N - 1]))
