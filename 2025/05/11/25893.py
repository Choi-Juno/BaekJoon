n = int(input())

for _ in range(n):
    double = 0
    a, b, c = map(int, input().split())
    if a >= 10:
        double += 1
    if b >= 10:
        double += 1
    if c >= 10:
        double += 1

    print(a, b, c)
    if double == 1:
        print("double")
    elif double == 2:
        print("double-double")
    elif double == 3:
        print("triple-double")
    else:
        print("zilch")
    print()
