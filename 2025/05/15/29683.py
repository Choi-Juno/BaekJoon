n, A = map(int, input().split())

lst = list(map(int, input().split()))
ticket = 0

for i in range(n):
    if lst[i] >= A:
        ticket += lst[i] // A

print(ticket)
