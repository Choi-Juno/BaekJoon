N = int(input())
S = input()

if S.endswith("G"):
    print(S[:-1])
else:
    print(S + "G")
