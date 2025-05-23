N = int(input())
count = 0
result = 666

while True:
    if "666" in str(result):
        count += 1
    if count == N:
        break
    result += 1

print(result)
