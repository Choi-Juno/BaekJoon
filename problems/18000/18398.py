T = int(input())

for _ in range(T):
    for _ in range(int(input())):
        a, b = map(int, input().split())
        print(a + b, a * b)
