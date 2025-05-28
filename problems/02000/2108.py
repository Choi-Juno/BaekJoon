import sys
import collections

N = int(sys.stdin.readline())

numbers = [int(sys.stdin.readline()) for _ in range(N)]
numbers.sort()

print(round(sum(numbers) / N))
print(numbers[N // 2])

freq = collections.Counter(numbers).most_common()

if len(freq) > 1:
    if freq[0][1] == freq[1][1]:
        print(freq[1][0])
    else:
        print(freq[0][0])
else:
    print(freq[0][0])

print(numbers[-1] - numbers[0])
