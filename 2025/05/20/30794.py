lv, verdict = input().split()

lv = int(lv)
score = {"miss": 0, "bad": 200, "cool": 400, "great": 600, "perfect": 1000}

print(score[verdict] * lv)
