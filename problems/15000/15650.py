N, M = map(int, input().split())

seq = []


def dfs(start):
    if len(seq) == M:
        print(" ".join(map(str, seq)))
        return

    for i in range(start, N + 1):
        if i not in seq:
            seq.append(i)
            dfs(i + 1)
            seq.pop()


dfs(1)
