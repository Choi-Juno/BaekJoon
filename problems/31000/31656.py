str = input()

print(str[0], end="")
for i in range(1, len(str)):
    if str[i] == str[i - 1]:
        continue
    print(str[i], end="")
