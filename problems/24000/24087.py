S = int(input())
A = int(input())
B = int(input())

if S <= A:
    print(250)
elif (S - A) % B == 0:
    print((S - A) // B * 100 + 250)
else:
    print((S - A) // B * 100 + 250 + 100)
