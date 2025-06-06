N = int(input())

prime_list = []

while N != 1:
    for i in range(2, N + 1):
        if N % i == 0:
            prime_list.append(i)
            N = N // i
            break

for i in prime_list:
    print(i)
