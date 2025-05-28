n = int(input())
order = []

for _ in range(n):
    x, y = map(int, input().split())
    order.append((x, y))

order.sort(key=lambda x: (x[1], x[0]))
for i in order:
    print(i[0], i[1])
