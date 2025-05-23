N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

shirts = 0
pen_bundle = 0

for i in size:
    if i == 0:
        continue
    elif i % T == 0:
        shirts += i // T
    else:
        shirts += i // T + 1

pen_bundle = N // P
pen = N % P

print(shirts)
print(pen_bundle, pen)
