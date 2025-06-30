T = int(input())


def dfs(start_x, start_y, graph, visited, M, N):
    stack = [(start_x, start_y)]
    visited[start_x][start_y] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    stack.append((nx, ny))


for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * N for _ in range(M)]
    visited = [[0] * N for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    count = 0
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j, graph, visited, M, N)
                count += 1

    print(count)
