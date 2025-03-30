N = int(input())

score = list(map(int, input().split()))

maxScore = max(score)

for i in range(N):
    score[i] = score[i] / maxScore * 100

print(sum(score) / N)
