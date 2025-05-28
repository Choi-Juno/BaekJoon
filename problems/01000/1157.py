import collections

str = input().lower()

freq = collections.Counter(str).most_common()

if len(freq) > 1:
    if freq[0][1] == freq[1][1]:
        print("?")
    else:
        print(freq[0][0].upper())
else:
    print(freq[0][0].upper())
