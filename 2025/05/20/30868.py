N = int(input())

for _ in range(N):
    votes = int(input())
    print("++++ " * (votes // 5) + "|" * (votes % 5))
