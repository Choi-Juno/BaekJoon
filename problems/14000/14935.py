x = int(input())


def f(x):
    return int(str(x)[0]) * len(str(x))


while True:
    prevFx = f(x)
    if prevFx == x:
        print("FA")
        break
    x = prevFx
