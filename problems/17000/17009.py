a3 = int(input())
a2 = int(input())
a1 = int(input())
b3 = int(input())
b2 = int(input())
b1 = int(input())

if a1 + a2 * 2 + a3 * 3 > b1 + b2 * 2 + b3 * 3:
    print("A")
elif a1 + a2 * 2 + a3 * 3 < b1 + b2 * 2 + b3 * 3:
    print("B")
else:
    print("T")
