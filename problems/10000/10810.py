N, M = map(int, input().split())

array = [0] * N

for i in range(M):
    i, j, k = map(int, input().split())
    for i in range(i - 1, j):
        array[i] = k

for i in range(N):
    print(array[i], end=" ")
