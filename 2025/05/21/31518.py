N = int(input())
count = 0

for _ in range(3):
    line = list(map(int, input().split()))
    if 7 in line:
        count += 1

if count == 3:
    print(777)
else:
    print(0)
