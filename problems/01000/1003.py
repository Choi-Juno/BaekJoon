def count_zero_one(n):
    if n == 0:
        return (1, 0)  # 0이 1번, 1이 0번
    if n == 1:
        return (0, 1)  # 0이 0번, 1이 1번

    # 피보나치 수열의 각 숫자에서 0과 1이 등장하는 횟수를 저장
    dp = [(0, 0)] * (n + 1)
    dp[0] = (1, 0)  # 0이 1번, 1이 0번
    dp[1] = (0, 1)  # 0이 0번, 1이 1번

    # 피보나치 수열을 계산하면서 0과 1의 등장 횟수도 함께 계산
    for i in range(2, n + 1):
        # i번째 피보나치 수는 i-1번째와 i-2번째의 합
        # 따라서 0과 1의 등장 횟수도 각각 더해줌
        dp[i] = (dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1])

    return dp[n]


T = int(input())

for _ in range(T):
    N = int(input())
    a, b = 1, 0
    for i in range(N):
        a, b = b, a + b

    print(a, b)
