n, k = map(int, input().split())

ammo = 0
saveAmmo = 0

for _ in range(n):
    action = input()
    if action == "ammo":
        ammo += k
    elif action == "save":
        saveAmmo = ammo
    elif action == "load":
        ammo = saveAmmo
    elif action == "shoot":
        ammo -= 1

    print(ammo)
