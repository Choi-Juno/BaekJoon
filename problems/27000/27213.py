m = int(input())
n = int(input())

cell = m * 2 + n * 2 - 4
if m == 1 or n == 1:
    cell = max(m, n)
print(cell)
