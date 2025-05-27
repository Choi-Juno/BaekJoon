reLecture = input()
reLecture = reLecture[:5]
count = 0

for i in range(int(input())):
    lecture = input()
    if lecture[:5] == reLecture:
        count += 1

print(count)
