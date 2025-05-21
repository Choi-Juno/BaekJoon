def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


N = int(input())

for _ in range(N):
    number = int(input())
    print(str(factorial(number))[-1])
