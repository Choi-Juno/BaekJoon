computer = int(input())
connect = int(input())


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [[] for _ in range(computer + 1)]
visited = [False] * (computer + 1)

for _ in range(connect):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph, 1, visited)
print(visited.count(True) - 1)
