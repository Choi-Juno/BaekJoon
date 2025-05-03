day = int(input())

lst = list(map(int, input().split()))

count = 0

for i in range(len(lst)):
    if lst[i] % 10 == day:
        count += 1

print(count)
