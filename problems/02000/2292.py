N = int(input())
depth = 1
count = 1

while True:
    if count < N:
        count += 6 * depth
        depth += 1
    else:
        print(depth)
        break
