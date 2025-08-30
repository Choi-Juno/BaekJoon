from collections import deque


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    papers = list(map(int, input().split()))

    # (우선순위, 원래 인덱스) 형태로 queue 생성
    queue = deque([(papers[i], i) for i in range(n)])

    count = 0
    while queue:
        current = queue.popleft()

        # 현재 문서보다 중요도가 높은 문서가 큐에 있는지 확인
        if any(current[0] < item[0] for item in queue):
            queue.append(current)
        else:
            count += 1
            # 원래 인덱스와 비교 후 인쇄 횟수 출력
            if current[1] == m:
                print(count)
                break
