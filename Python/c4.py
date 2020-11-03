#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'decryptPassword' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def Convert(string): 
    list1=[] 
    list1[:0]=string 
    return list1 

def decryptPassword(s):
    # Write your code here
    n = len(s)
    s = Convert(s)
    for i in range(n):
        if s[i] == '*':
            s[i-1], s[i-2] = s[i-2], s[i-1]
        elif s[i] == '0':
            s[i] = s[0]
            s[0] = '0'

    a = ''
    for i in range(n):
        if s[i] != '0' and s[i] != '*':
            a += s[i]
    return a

if __name__ == '__main__':
    s = input()
    result = decryptPassword(s)
    print(result)

