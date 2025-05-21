n = int(input())

lst = list(map(float, input().split()))
total = 0

for i in range(n):
    total += lst[i] ** 3

print(total ** (1 / 3))
