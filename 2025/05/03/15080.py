start = input()
end = input()

start_hour, start_minute, start_second = map(int, start.split(":"))
end_hour, end_minute, end_second = map(int, end.split(":"))

start_time = start_hour * 3600 + start_minute * 60 + start_second
end_time = end_hour * 3600 + end_minute * 60 + end_second

duration = end_time - start_time

if duration < 0:
    duration += 24 * 3600

print(duration)
