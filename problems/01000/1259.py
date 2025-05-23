while True:
    number = input()
    if number == "0":
        break
    else:
        if number == number[::-1]:
            print("yes")
        else:
            print("no")
