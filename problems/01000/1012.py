import sys

sys.setrecursionlimit(10000)

T = int(input())

complex_list = []


def dfs(x, y):
    visited[x][y] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                dfs(nx, ny)

    return 1


for _ in range(T):
    complex_list = []
    M, N, K = map(int, input().split())
    graph = [[0] * N for _ in range(M)]
    visited = [[0] * N for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1 and visited[i][j] == 0:
                complex_list.append(dfs(i, j))

    print(len(complex_list))
