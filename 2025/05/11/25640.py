jinho = input()

N = int(input())
count = 0

for _ in range(N):
    MBTI = input()
    if MBTI == jinho:
        count += 1

print(count)
