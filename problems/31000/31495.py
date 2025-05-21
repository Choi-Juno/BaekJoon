str = input().strip()

if str[0] == '"' and str[-1] == '"' and len(str) >= 3 and " ":
    print(str[1:-1])
else:
    print("CE")
