#!/bin/python3


import os


# Complete the minimumSwaps function below.
# my result in 2 cycles, works normal
# def minimum_swaps(a_list):
#     swaps = 0
#     len_a_list = len(a_list)
#     for i in range(len_a_list):
#         min_index = i
#         for k in range(i, len_a_list):
#             if a_list[k] < a_list[min_index]:
#                 min_index = k
#         if min_index != i:
#             a_list[i], a_list[min_index] = a_list[min_index], a_list[i]
#             swaps += 1
# 
#     return swaps

#  code stolen from comments with one cycle
def minimum_swaps(arr):
    ref_arr = sorted(arr)
    index_dict = {v: i for i,v in enumerate(arr)}
    swaps = 0

    for i, v in enumerate(arr):
        correct_value = ref_arr[i]
        if v != correct_value:
            to_swap_ix = index_dict[correct_value]
            arr[to_swap_ix], arr[i] = arr[i], arr[to_swap_ix]
            index_dict[v] = to_swap_ix
            index_dict[correct_value] = i
            swaps += 1

    fptr.write(str(index_dict) + '\n')
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    fptr.write(str(minimum_swaps(arr)) + '\n')
    fptr.close()
