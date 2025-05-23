N, M = map(int, input().split())
cards = list(map(int, input().split()))

result = 0
max = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            sum = cards[i] + cards[j] + cards[k]
            if sum > M:
                continue
            else:
                if max <= sum:
                    max = sum

print(max)
