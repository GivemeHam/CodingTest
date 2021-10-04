# 단어수학
import sys

n = int(sys.stdin.readline())

words = []
wordsDict = {}
valueArray = []

for i in range(n):
    words.append(sys.stdin.readline().rstrip())

for word in words:
    for i in range(len(word)):
        if word[i] in wordsDict:
            wordsDict[word[i]] += 10**(len(word)-i-1)
        else:
            wordsDict[word[i]] = 10**(len(word)-i-1)

for val in wordsDict.values():
    valueArray.append(val)

valueArray.sort(reverse=True)
answer = 0
pows = 9
for i in valueArray:
    answer += pows * i
    pows -= 1
print(answer)
