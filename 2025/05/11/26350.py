N = int(input())

for _ in range(N):
    d, *penny = map(int, input().split())
    flag = True

    for i in range(1, d):
        if (penny[i - 1] * 2) <= penny[i]:
            flag = True
        else:
            flag = False
            break

    if flag:
        print("Denominations:", *penny)
        print("Good coin denominations!\n")
    else:
        print("Denominations:", *penny)
        print("Bad coin denominations!\n")
