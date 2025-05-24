T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    # 0층 사람 수
    floor0 = [i for i in range(1, n + 1)]

    # 층수 만큼 반복
    for i in range(k):
        # 호실
        for j in range(1, n):
            floor0[j] += floor0[j - 1]

    print(floor0[-1])
