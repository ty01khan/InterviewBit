#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    l = len(q)
    for i in range(l): 
        k = 0
        if q[i] > i+3 or q[i] < i-1:
            k = 1
            break
    if k == 1:
        return "Too chaotic"

    A = [x+1 for x in range(l)]
    cnt = 0
    i = 0
    while i < l:
        if q[i] == i+1:
            i = i+1
            continue
        
        if i+1 < len(q):
            if q[i+1] == i+1:
                if q[i] == i+2:
                    q[i+1] = i+2
                    q[i] = i+1
                    cnt += 1
                    i += 2
                else:
                    q[i+1] = q[i]
                    q[i] = i+1
                    cnt += 1
                    i += 1
        if i+2 < len(q):
            if q[i+2] == i+1:
                a = q[i+1]
                q[i+1] = i+1
                q[i+2] = a
                q[i+1] = q[i]
                q[i] = i+1
                cnt += 2
                i += 1
        '''ind = q.index(i+1)
        if ind == i+1:
            q[i+1] = q[i]
            q[i] = i+1
            cnt += 1
            i += 1
        else:
            a = q[i+1]
            q[i+1] = i+1
            q[i+2] = a
            q[i+1] = q[i]
            q[i] = i+1
            cnt += 2
            i += 1'''
        if q == A:
            break
    return cnt
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))

