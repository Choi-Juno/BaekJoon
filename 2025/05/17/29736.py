A, B = map(int, input().split())
K, X = map(int, input().split())

friend = 0

for i in range(A, B + 1):
    if K - X <= i <= K + X:
        friend += 1

print(friend if friend > 0 else "IMPOSSIBLE")
