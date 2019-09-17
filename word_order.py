#!/usr/bin/env python36

from collections import OrderedDict

words_dict = OrderedDict()
for i in range(int(input())):
    word = input()
    words_dict[word] = words_dict.get(word, 0) + 1

print(len(words_dict))
print(*words_dict.values())
