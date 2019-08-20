#!/usr/bin/env python36

from itertools import product

linesCount, module = map(int, input().split())
lists = [map(int, input().split()[1:]) for x in range(linesCount)]

results = map(lambda x: sum(i**2 for i in x)%module, product(*lists))
print(max(results))

