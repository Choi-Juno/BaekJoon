from collections import deque

N, K = map(int, input().split())

visited = [0] * 100001


def bfs(N, K):
    queue = deque()

    queue.append(N)  # 수빈이 출발점 queue에 추가
    visited[N] = 1

    while queue:
        x = queue.popleft()
        if x == K:
            return visited[x]

        # 이동할 수 있는 방향에 대해서
        # 범위 내에 있고, 방문하지 않은 점에 대해서
        for i in [x - 1, x + 1, x * 2]:
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[x] + 1
                queue.append(i)

    return -1  # 동생에게 도달할 수 없을 때


print(bfs(N, K) - 1)
