n = int(input())

n = n % 8
if n == 1:
    print(1)
elif n in [2, 0]:
    print(2)
elif n in [3, 7]:
    print(3)
elif n in [4, 6]:
    print(4)
else:
    print(5)
