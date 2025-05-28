N, M = map(int, input().split())

board = [input().rstrip() for _ in range(N)]

# 체스보드 기본형태
whiteBoard = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
]

minPaint = 64  # 최소 색칠 횟수

# 8x8 체스판 자르기
for i in range(N - 7):
    for j in range(M - 7):
        # 덧칠 횟수
        count = 0

        # 8 x 8 보드 정의
        for row in range(8):
            for col in range(8):
                if board[i + row][j + col] != whiteBoard[row][col]:
                    count += 1

        # 최소 색칠 횟수 갱신
        minPaint = min(minPaint, count, 64 - count)

print(minPaint)
