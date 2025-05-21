N = int(input())
for _ in range(N):
    string, i, j = input().split()
    print(string[: int(i)] + string[int(j) :])
