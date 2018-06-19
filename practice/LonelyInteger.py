#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the lonelyinteger function below.
def lonelyinteger(a):
    count = Counter(a)
    for i, j in count.items():
        if j < 2: 
            return(i)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
