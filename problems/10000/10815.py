import sys

input = sys.stdin.readline

N = int(input())
sangeun = set(map(int, input().split()))  # set으로 변경
M = int(input())
number = list(map(int, input().split()))

for i in number:
    if i in sangeun:  # set에서 O(1) 탐색
        print(1, end=" ")
    else:
        print(0, end=" ")
