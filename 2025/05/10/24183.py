a, b, c = map(int, input().split())

C4 = a * (0.229 * 0.324)
A3 = b * (0.297 * 0.42)
A4 = c * (0.21 * 0.297)

print(2 * C4 + 2 * A3 + A4)
