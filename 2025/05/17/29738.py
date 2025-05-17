T = int(input())

for i in range(T):
    rank = int(input())
    round_name = (
        "World Finals"
        if rank <= 25
        else "Round 3" if rank <= 1000 else "Round 2" if rank <= 4500 else "Round 1"
    )
    print(f"Case #{i + 1}: {round_name}")
