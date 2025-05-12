a, b = map(int, input().split())

acer = 4840
corn = 5 * acer

print(a * b // corn if a * b % corn == 0 else a * b // corn + 1)
