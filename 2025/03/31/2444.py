Number = int(input())

for i in range(1, Number + 1):
    print(" " * (Number - i) + "*" * (2 * i - 1))

for i in range(Number - 1, 0, -1):
    print(" " * (Number - i) + "*" * (2 * i - 1))
