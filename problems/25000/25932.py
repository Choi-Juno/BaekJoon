n = int(input())

for _ in range(n):
    lst = input()
    who = ""

    if "17" in lst and "18" in lst:
        who += "both"
    elif "17" in lst:
        who += "zack"
    elif "18" in lst:
        who += "mack"
    else:
        who += "none"
    print(lst)
    print(who)
    print()
