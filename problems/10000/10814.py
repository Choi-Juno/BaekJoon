N = int(input())

order = []

for _ in range(N):
    age, name = input().split()
    order.append(((int(age)), name))

order.sort(key=lambda x: x[0])

for i in order:
    print(i[0], i[1])
