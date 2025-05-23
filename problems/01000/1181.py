N = int(input())
wordList = []

for _ in range(N):
    wordList.append(input())

wordList = list(set(wordList))
wordList.sort()
wordList.sort(key=len)

for i in wordList:
    print(i)
