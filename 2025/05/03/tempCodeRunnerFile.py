start = input()
end = input()

start_hour, start_minute, start_second = map(int, start.split(" : "))
end_hour, end_minute, end_second = map(int, end.split(" : "))

if start_hour > end_hour:
    end_hour += 24

if start_minute > end_minute:
    end_minute += 60
    end_hour -= 1

if start_second > end_second:
    end_second += 60
    end_minute -= 1

duration = (
    (end_hour - start_hour) * 3600
    + (end_minute - start_minute) * 60
    + (end_second - start_second)
)

print(duration)
