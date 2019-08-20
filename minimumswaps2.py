#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.

# my result in 2 cycles
# def minimumSwaps(alist):
#     swaps = 0
#     for i in range(len(alist)):
#         minIndex = i
#         for k in range(i, len(alist)):
#             if alist[k] < alist[minIndex]:
#                 minIndex = k
#         if minIndex != i:
#             alist[i], alist[minIndex] = alist[minIndex], alist[i]
#             swaps += 1
#
#     return swaps

#  code stolen from comments with one cycle
def minimumSwaps(arr):
    ref_arr = sorted(arr)
    index_dict = {v: i for i,v in enumerate(arr)}
    swaps = 0

    for i,v in enumerate(arr):
        correct_value = ref_arr[i]
        if v != correct_value:
            to_swap_ix = index_dict[correct_value]
            arr[to_swap_ix],arr[i] = arr[i], arr[to_swap_ix]
            index_dict[v] = to_swap_ix
            index_dict[correct_value] = i
            swaps += 1

    fptr.write(str(index_dict) + '\n')
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
