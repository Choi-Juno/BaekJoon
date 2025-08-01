fomula = input()

fomula = fomula.split("-")

answer = 0

x = sum(map(int, fomula[0].split("+")))
if fomula[0] == "-":
    answer -= x
else:
    answer += x
    for x in fomula[1:]:
        x = sum(map(int, x.split("+")))
        answer -= x

print(answer)
