a, b, c = map(int, input().split())

hypotenuse = max(a, b, c)
if a == b == c:
    print("2")
elif hypotenuse**2 == a**2 + b**2 + c**2 - hypotenuse**2:
    print("1")
else:
    print("0")
