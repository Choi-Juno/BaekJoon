N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

result = [[a + b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(A, B)]

for row in result:
    print(*row)
