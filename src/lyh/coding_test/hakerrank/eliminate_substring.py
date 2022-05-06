#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getFinalString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def getFinalString(s):
    # Write your code here
    
    while "AWS" in s:
        s = s.replace("AWS", "")

    if not s:
        return "-1"
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = getFinalString(s)

    fptr.write(result + '\n')

    fptr.close()
