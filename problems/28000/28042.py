word = list(input())
MOBIS = ["M", "O", "B", "I", "S"]
result = True

for i in MOBIS:
    if i not in word:
        result = False
        break

print("YES" if result else "NO")
