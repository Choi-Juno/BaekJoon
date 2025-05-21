N, M, K = map(int, input().split())

rabbit = N
dog = 0
i = 0

while True:
    rabbit += M
    dog += K
    i += 1
    if dog >= rabbit:
        print(i)
        break
