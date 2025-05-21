t1, m1, t2, m2 = map(int, input().split())

duration = (t2 - t1) * 60 + (m2 - m1)

if duration < 0:
    duration += 24 * 60

print(duration, duration // 30)
