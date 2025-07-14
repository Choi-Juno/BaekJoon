from collections import deque


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
inDegree = [0] * (N + 1)
queue = deque()
answer = []

# 그래프 생성
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    inDegree[B] += 1

# 진입 차수가 0인 노드 큐에 추가
for i in range(1, N + 1):
    if inDegree[i] == 0:
        queue.append(i)

# 위상 정렬 수행
while queue:
    temp = queue.popleft()
    answer.append(temp)

    for i in graph[temp]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            queue.append(i)

print(*answer)
