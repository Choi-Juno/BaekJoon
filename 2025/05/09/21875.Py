col = ["1", "2", "3", "4", "5", "6", "7", "8"]
row = ["a", "b", "c", "d", "e", "f", "g", "h"]

n = input()
m = input()

moveRow = row.index(n[0]) - row.index(m[0])
moveCol = col.index(n[1]) - col.index(m[1])

print(min(abs(moveRow), abs(moveCol)), max(abs(moveRow), abs(moveCol)))
