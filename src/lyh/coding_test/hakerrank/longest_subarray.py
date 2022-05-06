#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxLength' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#

def maxLength(a, k):
    # Write your code here
    len_list = list()
    for i in range(len(a)):
        sum_val, length = 0, 0
        for num in a[i:]:
            if sum_val + num <= k:
                sum_val += num
                length += 1
            else:
                break
        len_list.append(length)
    return max(len_list)
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    k = int(input().strip())

    result = maxLength(a, k)

    fptr.write(str(result) + '\n')

    fptr.close()
