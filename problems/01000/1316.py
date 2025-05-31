N = int(input())

count = N

for _ in range(N):
    str = input()
    checker = []

    for i in range(len(str) - 1):
        if str[i] == str[i + 1]:
            continue
        elif str[i] in str[i + 1 :]:
            count -= 1
            break

print(count)
