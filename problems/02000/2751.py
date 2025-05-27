import sys

numbers = []

for _ in range(int(sys.stdin.readline())):
    numbers.append(int(sys.stdin.readline()))

sortedNumber = sorted(numbers)

for i in range(len(sortedNumber)):
    print(sortedNumber[i])
