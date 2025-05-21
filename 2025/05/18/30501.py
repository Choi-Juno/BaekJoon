N = int(input())

murder = ""

for _ in range(N):
    name = input()
    if "S" in name:
        murder = name

print(murder)
