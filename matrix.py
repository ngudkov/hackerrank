#!/bin/env python36


# Complete the diagonalDifference function below.
def diagonal_difference(arr):

    primary_diagonal_summ = 0.0
    secondary_diagonal_summ = 0.0
    arr_len = len(arr)

    for i in range(arr_len):
        for j in range(arr_len):
            if i == j:
                primary_diagonal_summ += arr[i][j]
            if arr_len - 1 == i + j:
                secondary_diagonal_summ += arr[i][j]

    return abs(primary_diagonal_summ - secondary_diagonal_summ)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    fptr.write(str(diagonal_difference(arr)) + '\n')
    fptr.close()
