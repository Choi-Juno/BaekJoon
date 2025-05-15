PIECE_VALUE = {"k": 0, "q": 9, "r": 5, "b": 3, "n": 3, "p": 1, ".": 0}

black = 0
white = 0

for i in range(8):
    row = input()
    for piece in row:
        if row[piece].islower():
            black += PIECE_VALUE[row[piece]]
        else:
            white += PIECE_VALUE[row[piece].lower()]

print(white - black)
