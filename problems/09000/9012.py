N = int(input())

for _ in range(N):
    str = input()
    stack = []

    for s in str:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if stack:
            print("NO")
        else:
            print("YES")
