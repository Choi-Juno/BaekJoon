initial, additional = map(int, input().split())
n = int(input())

for _ in range(n):
    use = int(input())
    if use > 1000:
        bill = 1000 * initial + (use - 1000) * additional
        print(use, bill)
    else:
        bill = use * initial
        print(use, bill)
