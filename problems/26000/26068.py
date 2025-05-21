N = int(input())

count = 0

for _ in range(N):
    xi = input()
    date = int(xi[2:])
    if date <= 90:
        count += 1

print(count)
