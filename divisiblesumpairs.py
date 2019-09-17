#!/bin/env python36

import os

# Complete the divisibleSumPairs function below.
def divisible_sum_pairs(n, k, ar):
    count = 0
    ar_len = len(ar)
    for i in range(ar_len):
        for j in range(i, ar_len):
            if (ar[i] + ar[j]) % k == 0 and i < j:
                count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()
    n, k = int(nk[0]), int(nk[1])
    ar = list(map(int, input().rstrip().split()))

    result = divisible_sum_pairs(n, k, ar)
    fptr.write(str(result) + '\n')

    fptr.close()
