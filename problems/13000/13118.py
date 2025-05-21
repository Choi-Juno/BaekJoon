p1, p2, p3, p4 = map(int, input().split())

x, y, r = map(int, input().split())

if p1 == x:
    print(1)
elif p2 == x:
    print(2)
elif p3 == x:
    print(3)
elif p4 == x:
    print(4)
else:
    print(0)
