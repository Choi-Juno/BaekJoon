N = int(input())

list = []
count = 0

for _ in range(N):
    Start, End = map(int, input().split())
    list.append([Start, End])


list.sort(key=lambda x: [x[1], x[0]])
end_time = list[0][1]
count += 1

for i in range(1, N):
    start_time = list[i][0]
    if start_time < end_time:
        continue
    end_time = list[i][1]
    count += 1

print(count)
