for i in range(3, 0, -1):
    number = input()
    if number not in ["Fizz", "Buzz", "FizzBuzz"]:
        n = int(number) + i

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)
