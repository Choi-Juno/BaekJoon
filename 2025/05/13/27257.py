num = input()
index = 0

for i in range(len(num) - 1, -1, -1):
    if num[i] != "0":
        index = num[:i].count("0")
        break
print(index)
