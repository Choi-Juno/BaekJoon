a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

lst = [a, b, c, d, e]

for i in range(len(lst)):
    if lst[i] < 40:
        lst[i] = 40

print(sum(lst) // len(lst))
