N = int(input())

triangle = []

for _ in range(N):
    triangle.append(list(map(int, input().split())))

dp = [[0] * N for _ in range(N)]

dp[0][0] = triangle[0][0]

for i in range(1, N):  # i=1부터 시작 (i=0은 이미 초기화됨)
    for j in range(len(triangle[i])):
        if j == 0:
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
        elif j == len(triangle[i]) - 1:
            dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]


print(max(dp[N - 1]))
