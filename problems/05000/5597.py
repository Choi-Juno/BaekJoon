array = [0] * 30

for i in range(28):
    a = int(input())
    array[a - 1] = 1

for i in range(30):
    if array[i] == 0:
        print(i + 1)
