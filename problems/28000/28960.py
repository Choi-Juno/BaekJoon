h, l, a, b = map(int, input().split())

if (a <= l and b <= h * 2) or (b <= l and a <= h * 2):
    print("YES")
else:
    print("NO")
