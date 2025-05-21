N = int(input())

numbers = list(map(int, input().split()))

unique_sorted = sorted(set(numbers))

for num in unique_sorted:
    print(num)
