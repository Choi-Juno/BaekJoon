N = int(input())

scores = []

for _ in range(N):
    a, d, g = map(int, input().split())
    score = a * (d + g)
    if a == d + g:
        score *= 2
    scores.append(score)

print(max(scores))
