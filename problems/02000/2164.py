N = int(input())

numbers = [i for i in range(1, N + 1)]

count = 0

while True:
    if len(numbers) == 1:
        print(numbers[0])
    else:
        numbers.pop(0)
        numbers.append(numbers.pop(0))
