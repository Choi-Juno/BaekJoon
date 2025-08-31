N, M = map(int, input().split())

seq = []


def dfs(start):
    if len(seq) == M:
        print(" ".join(map(str, seq)))
        return

    for i in range(1, N + 1):
        seq.append(i)
        dfs(i)
        seq.pop()


dfs(1)
