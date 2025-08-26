import sys

input = sys.stdin.readline

N = int(input())

answer = 0
row = [0] * N


def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


def N_Queen(x):
    global answer

    if x == N:
        answer += 1
    else:
        for col in range(N):
            row[x] = col
            if check(x):
                N_Queen(x + 1)


N_Queen(0)
print(answer)
