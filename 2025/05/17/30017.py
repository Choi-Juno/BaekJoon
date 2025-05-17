A, B = map(int, input().split())

while A >= 2:
    if B >= A - 1:
        print(A * 2 - 1)
        break
    else:
        A -= 1
