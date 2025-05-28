n = int(input())
order = []

for _ in range(n):
    x, y = map(int, input().split())
    order.append((x, y))

order.sort()
for i in order:
    print(i[0], i[1])
