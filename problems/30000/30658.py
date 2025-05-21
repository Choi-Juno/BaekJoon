while True:
    team = int(input())
    if team == 0:
        break
    rank_list = [int(input()) for _ in range(team)]
    reversed_rank = reversed(rank_list)

    for rank in reversed_rank:
        print(rank)
    print(0)
