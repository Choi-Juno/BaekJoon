import sys

input = sys.stdin.readline

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

sum = [0]
tmp = 0

# 누적 합 계산
for i in numbers:
    tmp = tmp + i
    sum.append(tmp)

# 구간 합 계산
for _ in range(M):
    i, j = map(int, input().split())
    print(sum[j] - sum[i - 1])
