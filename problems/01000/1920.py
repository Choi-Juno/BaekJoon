import sys

N = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

guessNumber = list(map(int, sys.stdin.readline().split()))
numbers.sort()

for num in guessNumber:
    left, right = 0, N - 1
    isExist = False

    # 이진탐색
    while left <= right:
        mid = (left + right) // 2
        if num == numbers[mid]:
            isExist = True
            print(1)
            break
        elif num < numbers[mid]:
            right = mid - 1
        else:
            left = mid + 1

    if not isExist:
        print(0)
