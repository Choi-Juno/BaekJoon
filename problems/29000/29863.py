S = int(input())
W = int(input())

if S < 24 and S > 3:
    print(24 - S + W)
else:
    print(W - S)
