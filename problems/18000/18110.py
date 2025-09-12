import sys

input = sys.stdin.readline

T = int(input())

difficulty = sorted([int(input()) for _ in range(T)])

if T == 0:
    print(0)
else:
    trim = int((T * 0.15) + 0.5)
    average = sum(difficulty[trim : T - trim]) / (T - trim * 2)
    print(int(average + 0.5))
