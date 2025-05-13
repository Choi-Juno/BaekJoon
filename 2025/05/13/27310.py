str = input()

difficulty = len(str) + str.count(":") + str.count("_") * 5
print(difficulty)
