N = int(input())

for _ in range(N):
    year = int(input())
    if (year + 1) % (year % 100) == 0:
        print("Good")
    else:
        print("Bye")
