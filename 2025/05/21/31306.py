str = input()

vowels = (
    str.count("a") + str.count("e") + str.count("i") + str.count("o") + str.count("u")
)

print(vowels, str.count("y") + vowels)
