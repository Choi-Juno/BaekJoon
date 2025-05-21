N = int(input())

for _ in range(N):
    w, h, iteration = map(int, input().split())

    print(f"Data set: {w} {h} {iteration}")
    for _ in range(iteration):
        if w > h:
            w //= 2
        else:
            h //= 2

    if w > h:
        print(w, h)
    else:
        print(h, w)
    print()
