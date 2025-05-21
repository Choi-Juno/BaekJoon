from math import factorial

N = int(input())

second = factorial(N)

week = second // (7 * 24 * 60 * 60)

print(week)
