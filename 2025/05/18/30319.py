date = input().split("-")
print(date)

if date[1] == "09":
    if int(date[2]) <= 16:
        print("GOOD")
    else:
        print("TOO LATE")
elif int(date[1]) >= 10:
    print("TOO LATE")
else:
    print("GOOD")
