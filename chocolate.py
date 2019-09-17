#!/bin/env python36

import os

# Complete the birthday function below.
def birthday(s, d, m):
    variants_arr = []
    # return 0 if montth is bigger than array length
    variants = 0
    if len(s) < m:
        return variants
    # get all slices
    for i in range(len(s)):
        if (i - m + 1) >= 0:
            temp_arr = []
            for j in range(i - m + 1, i + 1):
                temp_arr.append(s[j])
            variants_arr.append(temp_arr)

    # calculate summ of bar numbers and eq it with birthday day
    for variant in variants_arr:
        if sum(variant) == d:
            variants += 1
    return variants


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    #chocolate arrray
    s = list(map(int, input().rstrip().split()))
    dm = input().rstrip().split()
    #birthday day
    d = int(dm[0])
    #bithday month
    m = int(dm[1])

    result = birthday(s, d, m)
    fptr.write(str(result) + '\n')

    fptr.close()
