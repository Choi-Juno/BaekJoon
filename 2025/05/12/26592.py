for _ in range(int(input())):
    area, base = map(float, input().split())
    length = 2 * area / base
    print(f"The height of the triangle is {length:.2f} units")
