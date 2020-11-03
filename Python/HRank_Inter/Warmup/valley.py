#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    Sum = 0
    i = 0
    v = 0
    while i < n:
        if Sum == 0 and i != 0:
            if s[i-1] == 'U':
                v += 1
        if s[i] == 'U':
            Sum += 1
        else:
            Sum += -1
        i += 1
    if Sum == 0 and i != 0:
        if s[n-1] == 'U':
            v += 1
    return v

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

