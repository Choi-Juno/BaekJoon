N, M = map(int, input().split())

array = [i for i in range(1, N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    temp = array[a - 1 : b]
    temp.reverse()
    array[a - 1 : b] = temp

for i in range(N):
    print(array[i], end=" ")
