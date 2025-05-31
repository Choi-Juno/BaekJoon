def self_number(n):
    x = list(str(n))
    result = 0
    for i in range(len(x)):
        result += int(x[i])
    result += n
    return result


results = set()
for i in range(1, 10001):
    results.add(self_number(i))

for i in range(1, 10001):
    if i not in results:
        print(i)
