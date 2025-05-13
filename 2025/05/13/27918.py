N = int(input())

D, P = 0, 0
game = list(input() for _ in range(N))

for i in game:
    if i == "D":
        D += 1
    elif i == "P":
        P += 1

    if abs(D - P) == 2:
        break


print(f"{D}:{P}")
