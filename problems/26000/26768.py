str = input()

literaToNumber = {
    "a": 4,
    "e": 3,
    "i": 1,
    "o": 0,
    "s": 5,
}

for i in range(len(str)):
    if str[i] in literaToNumber:
        print(literaToNumber[str[i]], end="")
    else:
        print(str[i], end="")
