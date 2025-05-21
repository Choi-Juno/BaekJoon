H1, B1 = map(int, input().split())
H2, B2 = map(int, input().split())

score1 = H1 * 3 + B1
score2 = H2 * 3 + B2

gap = abs(score1 - score2)

if score1 > score2:
    print(f"1 {gap}")
elif score1 < score2:
    print(f"2 {gap}")
else:
    print("NO SCORE")
