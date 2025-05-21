M = int(input())
D = int(input())

if M == 2:
    if D < 18:
        print("Before")
    elif D > 18:
        print("After")
    else:
        print("Special")
elif M < 2:
    print("Before")
else:
    print("After")
