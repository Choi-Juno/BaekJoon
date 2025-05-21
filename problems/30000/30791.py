vote = list(map(int, input().split()))
sixteen = vote[0]
count = 0

for i in range(1, len(vote)):
    diff = sixteen - vote[i]
    if diff <= 1000:
        count += 1

print(count)
