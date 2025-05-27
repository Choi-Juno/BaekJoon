N = int(input())

body = []
rank = [1] * N

body = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if body[i][0] < body[j][0] and body[i][1] < body[j][1]:
            rank[i] += 1

print(*rank)
