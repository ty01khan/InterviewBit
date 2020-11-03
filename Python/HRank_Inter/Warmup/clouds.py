#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    n = len(c)
    if n == 1:
        return 0
    if n == 2:
        return 1
    m = 0
    i = 0
    while i < n-1:
        if i != n-2:
            if c[i+2] == 0:
                m += 1
                i += 2
                continue
        if c[i+1] == 0:
            i += 1
            m += 1
            continue
    return m
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

