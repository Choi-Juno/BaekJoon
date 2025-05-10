str = input()

answer = ""
pos = 0

while pos < len(str):
    answer += str[pos]
    pos += ord(str[pos]) - ord("A") + 1

print(answer)
