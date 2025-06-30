from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]


def BFS(x, y):
    # 상하좌우 이동 벡터
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 벗어나는 경우
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 벽익거나 이미 방문한 경우
            if maze[nx][ny] != 1:
                continue

            # 이동 가능하면 거리 갱신 + 큐에 추가
            maze[nx][ny] = maze[x][y] + 1
            queue.append((nx, ny))

    return maze[N - 1][M - 1]


print(BFS(0, 0))
