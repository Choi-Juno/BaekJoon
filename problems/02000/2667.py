N = int(input())

graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
complex_list = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    visited[x][y] = 1
    complex_count = 1  # 자기 자신부터 시작
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                complex_count += dfs(nx, ny)

    return complex_count


# 전체 순회
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            complex_list.append(dfs(i, j))

print(len(complex_list))
for i in sorted(complex_list):
    print(i)
