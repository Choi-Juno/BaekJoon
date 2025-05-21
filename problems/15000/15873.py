number = input()

if len(number) == 2:
    print(int(number[0]) + int(number[1]))
elif len(number) == 3:
    if number[1] == "0":
        print(10 + int(number[2]))
    else:
        print(int(number[0]) + 10)
else:
    print(20)
