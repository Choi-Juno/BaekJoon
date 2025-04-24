while 1:
    size = int(input())
    if size == 0:
        break
    else:
        block = 0
        for i in range(size):
            block += i + 1
        print(block)
