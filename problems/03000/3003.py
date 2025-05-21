piece = list(map(int, input().split()))
correct = [1, 1, 2, 2, 2, 8]

for i in range(len(piece)):
    if piece[i] == correct[i]:
        print(0, end=" ")
    elif piece[i] < correct[i]:
        print(correct[i] - piece[i], end=" ")
    else:
        print(correct[i] - piece[i], end=" ")
