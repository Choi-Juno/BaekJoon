from collections import Counter

count = Counter(input() for _ in range(9))
print("Lion" if count["Lion"] > count["Tiger"] else "Tiger")
