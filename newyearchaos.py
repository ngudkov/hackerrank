#!/bin/env python36


def insertion_sort(a_list):
    result = 0
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            result += 1
            a_list[position] = a_list[position - 1]
            position -= 1
        a_list[position] = current_value
    return result


# Complete the minimumBribes function below.
def minimum_bribes(q):

    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
            return "Too chaotic"

    return insertion_sort(q)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        queue = list(map(int, input().rstrip().split()))

        print(minimum_bribes(queue))
