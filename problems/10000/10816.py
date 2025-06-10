import sys

n = int(sys.stdin.readline())
cards = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
candidates = map(int, sys.stdin.readline().split())

count = {}

for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for target in candidates:
    result = count.get(target, 0)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")

print()
