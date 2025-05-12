for _ in range(int(input())):
    str = input()
    print(str if str.endswith(".") else str + ".")
