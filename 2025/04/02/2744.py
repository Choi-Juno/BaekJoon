String = input()

for i in String:
    if i.isupper():
        print(i.lower(), end="")
    else:
        print(i.upper(), end="")
