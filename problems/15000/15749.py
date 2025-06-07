import itertools

N, M = map(int, input().split())
nums = [i for i in range(1, N + 1)]

array = itertools.permutations(nums, M)

for i in array:
    for j in i:
        print(j, end=" ")
    print()
