N, M = map(int, input().split())

total = 0

for _ in range(N):
    question = input()
    good = question.count("O")
    bad = question.count("X")
    if good > bad:
        total += 1

print(total)
