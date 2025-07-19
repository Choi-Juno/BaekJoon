N, K = map(int, input().split())

queue = [i for i in range(1, N + 1)]
result = []
index = 0

while queue:
    # K - 1번째까지 이동
    index += K - 1

    # 인덱스가 범위를 벗어날 경우
    if index >= len(queue):
        index %= len(queue)

    result.append(str(queue.pop(index)))

print(f'<{", ".join(result)}>')
