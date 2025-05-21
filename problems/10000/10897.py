str = input()

count = 0

for i in range(len(str)):
    if str[i] in "aeiou":
        count += 1

print(count)
