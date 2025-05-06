a = int(input())
x = int(input())
b = int(input())
y = int(input())
T = int(input())

bicycleA = a + max((T - 30), 0) * x * 21
bicycleB = b + max((T - 45), 0) * y * 21

print(bicycleA, bicycleB)
