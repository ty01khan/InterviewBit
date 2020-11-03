#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the makingAnagrams function below.
if __name__ == '__main__':

    s1 = input()

    s2 = input()
    c1 = Counter(s1)
    c2 = Counter(s2)
    common = c1 & c2
    x = 0
    print(common['c'])
    for i in common:
    	print(i)
    	x = x + common[i]
    
    print( len(s1) - 2*x + len(s2))
