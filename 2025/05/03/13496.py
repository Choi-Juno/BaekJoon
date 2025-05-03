K = int(input())

money = 0
for i in range(K):
    n, s, d = map(int, input().split())
    for j in range(n):
        di, vi = map(int, input().split())

        distance = di - (s * d)

        if distance <= 0:
            money += vi

    print(f"Data Set {i+1}: ")
    print(money)
    money = 0
    print()
