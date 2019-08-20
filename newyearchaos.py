#!/bin/env python36

import math
import os
import random
import re
import sys

def insertionSort(alist):
    result = 0
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            result  += 1
            alist[position] = alist[position - 1]
            position -= 1
        alist[position] = currentvalue
    return result

# Complete the minimumBribes function below.
def minimumBribes(q):
    # check if the queue is too chaotic
    for i in range(len(q)):
        if  q[i] - (i + 1) > 2:
            return "Too chaotic"

    return insertionSort(q)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
