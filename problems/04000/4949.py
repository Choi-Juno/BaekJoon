while True:
    sentence = input()

    if sentence == ".":
        break

    stack = []
    for char in sentence:
        if char == "(" or char == "[":
            stack.append(char)
        elif char == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(char)
        elif char == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(char)

    if len(stack) != 0:
        print("no")
    else:
        print("yes")
