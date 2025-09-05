import sys

input = sys.stdin.readline

T = int(input())

S = set()

for _ in range(T):
    command = input().split()

    match command[0]:
        case "add":
            S.add(int(command[1]))
        case "remove":
            S.discard(int(command[1]))
        case "check":
            if int(command[1]) in S:
                print(1)
            else:
                print(0)
        case "toggle":
            x = int(command[1])
            if x in S:
                S.remove(x)
            else:
                S.add(x)
        case "all":
            S = set(range(1, 21))
        case "empty":
            S = set()
