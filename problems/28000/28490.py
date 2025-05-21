N = int(input())

frameSize = []

for _ in range(N):
    w, h = map(int, input().split())

    frameSize.append(w * h)

print(max(frameSize))
