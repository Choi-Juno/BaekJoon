t = int(input())

for _ in range(t):
    lt, wt, le, we = map(int, input().split())
    print(
        "TelecomParisTech"
        if lt * wt > le * we
        else "Eurecom" if lt * wt < le * we else "Tie"
    )
