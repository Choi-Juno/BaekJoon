K, N = map(int, input().split())

cables = [int(input()) for _ in range(K)]


def binary_search(start, end):
    count = 0
    while start <= end:
        mid = (start + end) // 2
        count = 0

        for i in cables:
            count += i // mid
        if count >= N:
            start = mid + 1
        else:
            end = mid - 1

    return end


print(binary_search(1, max(cables)))
