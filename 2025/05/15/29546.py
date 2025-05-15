N = int(input())

picture = []

for _ in range(N):
    picture.append(input())

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(*picture[a - 1 : b], sep="\n")
