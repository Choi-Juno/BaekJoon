play = input()

result = [play[i : i + 2] for i in range(0, len(play), 2)]
pointA = 0
pointB = 0

for i in range(len(result)):
    if result[i][0] == "A":
        pointA += int(result[i][1])
    else:
        pointB += int(result[i][1])


if pointA > pointB:
    print("A")
else:
    print("B")
