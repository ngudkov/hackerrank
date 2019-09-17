#!/usr/bin/env python36

from collections import OrderedDict, Counter

wordsDict = OrderedDict()
for i in range(int(input())):
    word = input()
    wordsDict[word] = wordsDict.get(word, 0) + 1

print(len(wordsDict))
print(*wordsDict.values())
