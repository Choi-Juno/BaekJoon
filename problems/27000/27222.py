N = int(input())

isExercise = list(map(int, input().split()))
total = 0

for i in range(N):

    before, after = map(int, input().split())
    gap = after - before

    if isExercise[i] == 1:
        if gap >= 1:
            total += gap

print(total)
