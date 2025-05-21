meme = [
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you",
    "Never gonna stop",
]

flag = False
n = int(input())

for i in range(n):
    hack = input()
    if hack not in meme:
        flag = True
        break

print("Yes" if flag else "No")
