T = int(input())

dp = [0] * 1000001

dp[1], dp[2], dp[3] = 1, 1, 1
dp[4], dp[5] = 2, 2


for _ in range(T):
    N = int(input())

    for i in range(6, N + 1):
        dp[i] = dp[i - 1] + dp[i - 5]

    print(dp[N])
