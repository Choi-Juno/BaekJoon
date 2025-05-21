array = [0] * 10

for i in range(10):
    a = int(input())
    array[i] = a % 42

array = set(array)

print(len(array))
