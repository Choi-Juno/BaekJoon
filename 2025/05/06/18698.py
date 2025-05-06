T = int(input())
U = 0
for i in range(T):
    str = input()
    down = str.find("D")
    if down == 0:
        print(0)
    elif down == -1:
        print(len(str))
    else:
        print(down)
