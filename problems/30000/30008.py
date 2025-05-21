N, K = map(int, input().split())
G = list(map(int, input().split()))

D = []

for i in range(K):
    D.append(int((G[i] * 100) / N))

    if 0 <= D[i] <= 4:
        D[i] = 1
    elif 4 < D[i] <= 11:
        D[i] = 2
    elif 11 < D[i] <= 23:
        D[i] = 3
    elif 23 < D[i] <= 40:
        D[i] = 4
    elif 40 < D[i] <= 60:
        D[i] = 5
    elif 60 < D[i] <= 77:
        D[i] = 6
    elif 77 < D[i] <= 89:
        D[i] = 7
    elif 89 < D[i] <= 96:
        D[i] = 8
    elif 96 < D[i] <= 100:
        D[i] = 9

print(*D)
