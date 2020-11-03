#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    k = len(s)
    if s.count('a') == k:
        return n
    c = s.count('a')
    c = c*(int(n/k))
    i = n%k
    s = s[0:i]
    c += s.count('a')
    return c
if __name__ == '__main__':

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(result)
