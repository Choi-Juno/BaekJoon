N = int(input())

price = []
total = 0

for _ in range(N):
    price.append(int(input()))
M = int(input())
for _ in range(M):
    menu = int(input())
    total += price[menu - 1]

print(total)
