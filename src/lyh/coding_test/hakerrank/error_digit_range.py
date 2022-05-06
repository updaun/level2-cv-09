#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findRange' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER num as parameter.
#
def findMin(num):
    temp = str(num)
    for i, token in enumerate(temp):
        if int(token) > 1:
            if i == 0:
                return int(temp.replace(token, "1"))
            return int(temp.replace(token, "0"))
    return num
    
def findMax(num):
    temp = str(num)
    re_token = str()
    for token in temp:
        if int(token) < 9:
            re_token = token
            break
        
    if len(temp) == 1:
        return 9
    return int(temp.replace(re_token, "9"))

def findRange(num):
    # Write your code here
    print(num)
    return findMax(num) - findMin(num)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num = int(input().strip())

    result = findRange(num)

    fptr.write(str(result) + '\n')

    fptr.close()
