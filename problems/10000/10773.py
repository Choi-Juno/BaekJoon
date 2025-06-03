N = int(input())

total = []

for i in range(N):
    num = int(input())
    if num == 0:
        total.pop()
    else:
        total.append(num)

print(sum(total))
