k = int(input())

commission = 25 + k * 0.01

if commission <= 100:
    print(100)
elif commission >= 2000:
    print(2000)
else:
    print(f"{commission:.2f}")
