tiles = int(input())

i = 1
while i * i <= tiles:
    i += 1

print(f"The largest square has side length {i-1}.")
