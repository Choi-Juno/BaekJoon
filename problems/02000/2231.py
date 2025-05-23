num = int(input())
distribution = 0

for i in range(1, num):
    numberLength = len(str(i))
    for j in range(numberLength):
        distribution += int(str(i)[j])

    distribution += i

    if distribution == num:
        print(i)
        break
    else:
        distribution = 0

if distribution == 0:
    print(0)
