T = int(input())

for _ in range(T):
    str = input()
    score = 0
    sum = 0

    for i in str:
        if i == "O":
            score += 1
        else:
            score = 0
        sum += score

    print(sum)
