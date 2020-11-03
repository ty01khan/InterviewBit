#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr,i,cnt):
    A = arr[0:len(arr)]
    A.sort()
    if arr[0] != i+1:
        j = arr.index(i+1)
        arr[j] = arr[0]
        arr[0] = i+1
        cnt += 1
    if A == arr:
        return cnt
    i += 1
    return minimumSwaps(arr[i:len(arr)],i,cnt)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr,0,0)

    fptr.write(str(res) + '\n')

    fptr.close()

