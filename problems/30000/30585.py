h, w = map(int, input().split())

f, b = 0, 0

for _ in range(h):
    popit = input()
    f += popit.count("1")
    b += popit.count("0")

print(min(f, b))
