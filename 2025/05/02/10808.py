str = input()

count = [0] * 26

for i in range(len(str)):
    count[ord(str[i]) - 97] += 1

for i in range(len(count)):
    print(count[i], end=" ")
