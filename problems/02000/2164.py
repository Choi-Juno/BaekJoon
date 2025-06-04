from collections import deque

N = int(input())

numbers = deque(range(1, N + 1))

while len(numbers) > 1:
    numbers.popleft()  # 첫 번째 카드 제거
    numbers.append(numbers.popleft())  # 두 번째 카드를 맨 뒤로 이동

print(numbers[0])
