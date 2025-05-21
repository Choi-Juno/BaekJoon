birth = list(map(int, input().split()))
current = list(map(int, input().split()))

YoonAge = (
    (current[0] - birth[0])
    if (current[1] > birth[1]) or (current[1] == birth[1] and current[2] >= birth[2])
    else (current[0] - birth[0] - 1)
)

koreanAge = current[0] - birth[0] + 1

yearAge = current[0] - birth[0]

print(YoonAge)
print(koreanAge)
print(yearAge)
