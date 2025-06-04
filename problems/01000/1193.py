X = int(input())

# 몇 번째 줄인지 구하기
line = 1
while X > line:
    X -= line
    line += 1

a = X
b = line - X + 1

if line % 2 == 0:
    print(f"{a}/{b}")
else:
    print(f"{b}/{a}")
