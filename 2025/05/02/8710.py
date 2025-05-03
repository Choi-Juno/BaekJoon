k, w, m = map(int, input().split())

diff = w - k
if diff % m == 0:
    print(diff // m)
else:
    print(diff // m + 1)
