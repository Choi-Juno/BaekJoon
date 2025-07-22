import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)
result = 0  # 최종 절단기 높이

while start <= end:
    mid = (start + end) // 2  # 절단기 높이
    total = sum(
        max(0, tree - mid) for tree in trees
    )  # 절단기 높이보다 큰 나무는 잘라서 가져감

    # 이분탐색
    if total < M:
        end = mid - 1  # 절단기 높이를 낮춤
    else:
        result = mid
        start = mid + 1  # 절단기 높이를 높임

print(result)
