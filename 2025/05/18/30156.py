T = int(input())

for i in range(T):
    balloon = input()

    print(min(balloon.count("a"), balloon.count("b")))
