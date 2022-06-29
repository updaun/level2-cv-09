# source: https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    lr_diag_sum = 0
    rl_diag_sum = 0
    
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            
            if r == c:
                lr_diag_sum += arr[r][c]
                
            if r + c == len(arr) - 1:
                rl_diag_sum += arr[r][c]
            
    #     arr[r].reverse()
    
    # for r in range(len(arr)):
    #     for c in range(len(arr[r])):
            
    #         if r == c:
    #             rl_diag_sum += arr[r][c]
                
    return abs(lr_diag_sum - rl_diag_sum)
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
