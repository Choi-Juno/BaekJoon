newCase = int(input())
newHospital = int(input())

if newCase <= 50 and newHospital <= 10:
    print("White")
elif newHospital > 30:
    print("Red")
else:
    print("Yellow")
