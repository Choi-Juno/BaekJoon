N = int(input())
numberList = list(map(int, input().split()))

happinesePoint = sum(1 if number % 2 == 0 else -1 for number in numberList)

print("Happy" if happinesePoint > 0 else "Sad")
