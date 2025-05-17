N = int(input())

count = 0

for _ in range(N):
    str = input()
    if "OI" in str or "01" in str:
        count += 1

print(count)
