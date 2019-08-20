#!/bin/env python36

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):

    primaryDiagonalSumm = float(0)
    secondaryDiagonalSumm = float(0)
    arrLen = len(arr)
    print(str(arrLen))

    for i in range(arrLen):
        for j in range(arrLen):
            if i == j:
                print("adding to primary diagonal " + str(arr[i][j]))
                primaryDiagonalSumm += arr[i][j]
            if arrLen - 1 == i + j:
                print("adding to SECONDARY diagonal " + str(arr[i][j]))
                secondaryDiagonalSumm += arr[i][j]

    return abs(primaryDiagonalSumm - secondaryDiagonalSumm)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    a = len(arr)
    result = diagonalDifference(arr)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
