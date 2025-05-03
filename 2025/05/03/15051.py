A1 = int(input())
A2 = int(input())
A3 = int(input())

case1 = A1 * 0 + A2 * 2 + A3 * 4
case2 = A1 * 2 + A2 * 0 + A3 * 2
case3 = A1 * 4 + A2 * 2 + A3 * 0

print(min(case1, case2, case3))
