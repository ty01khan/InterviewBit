#!/bin/python3

import os
import sys

#
# Complete the primeCount function below.
#
def primeCount(n):
    #
    # Write your code here.
    #
    m = 1
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    p = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]
    j = 1
    i = 0
    
    while True:
        j *= p[i]
        
        if j > n:
            return i
        i += 1
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()

