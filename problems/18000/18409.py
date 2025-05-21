N = int(input())
S = input()
count = 0

for i in range(N):
    if S[i] in ["a", "e", "i", "o", "u"]:
        count += 1

print(count)
