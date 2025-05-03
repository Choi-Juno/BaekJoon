N = int(input())

for i in range(N):
    a, b, c, d = map(int, input().split())

    if b + c + d >= 55 and b >= 35 * 0.3 and c >= 25 * 0.3 and d >= 40 * 0.3:
        print(a, b + c + d, "PASS")
    else:
        print(a, b + c + d, "FAIL")
