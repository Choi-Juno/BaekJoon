N = int(input())

lst = list(map(int, input().split()))
total = 0

for i in range(len(lst)):
    if lst[i] > N:
        total += N
    else:
        total += lst[i]

print(total)
