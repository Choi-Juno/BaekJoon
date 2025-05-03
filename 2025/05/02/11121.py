N = int(input())

for i in range(N):
    a, b = input().split()

    for i in range(len(a)):
        if a[i] != b[i]:
            print("ERROR")
            break
    print("OK")
