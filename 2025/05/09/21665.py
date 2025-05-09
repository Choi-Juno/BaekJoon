n, m = map(int, input().split())

origin = []
invert = []

for _ in range(n):
    origin.append(input())

temp = input()

for _ in range(n):
    invert.append(input())

count = 0

for i in range(n):
    for j in range(m):
        if origin[i][j] == invert[i][j]:
            count += 1

print(count)
