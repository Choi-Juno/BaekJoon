T = int(input())

for _ in range(T):
    G, C, E = map(int, input().split())

    diff = E - C

    if diff > 0:
        if G == 1:
            print(diff * 1)
        elif G == 2:
            print(diff * 3)
        elif G == 3:
            print(diff * 5)
    else:
        print(0)
