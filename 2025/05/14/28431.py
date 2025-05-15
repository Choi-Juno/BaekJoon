socks = []

for _ in range(5):
    number = int(input())

    if number in socks:
        socks.remove(number)
    else:
        socks.append(number)

print(socks[0])
