depth = 0

for _ in range(4):
    platform = input().split()
    if platform[0] == "Es":
        depth += int(platform[1]) * 21
    elif platform[0] == "Stair":
        depth += int(platform[1]) * 17

print(depth)
