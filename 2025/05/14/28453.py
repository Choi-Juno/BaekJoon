N = int(input())

levelScope = []

level = list(map(int, input().split()))

for i in range(N):
    if level[i] == 300:
        levelScope.append(1)
    elif level[i] >= 275:
        levelScope.append(2)
    elif level[i] >= 250:
        levelScope.append(3)
    else:
        levelScope.append(4)

print(*levelScope)
