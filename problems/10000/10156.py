K, N, M = map(int, input().split())

diff = K * N - M

if diff > 0:
    print(diff)
else:
    print(0)
