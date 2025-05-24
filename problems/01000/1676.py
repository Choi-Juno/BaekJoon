from math import factorial

Nfact = factorial(int(input()))

Nfact = str(Nfact)
count = 0

for i in range(len(Nfact) - 1, -1, -1):
    if Nfact[i] == "0":
        count += 1
    else:
        break

print(count)
