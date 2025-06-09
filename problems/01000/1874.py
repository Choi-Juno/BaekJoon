N = int(input())

stack = []
result = []
find = True

now = 1
for _ in range(N):
    num = int(input())
    # Push
    while now <= num:
        stack.append(now)
        result.append("+")
        now += 1
    # Pop
    if stack and stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        find = False
        break

if find:
    for i in result:
        print(i)
else:
    print("NO")
