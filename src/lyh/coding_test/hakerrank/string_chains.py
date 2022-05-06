#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'longestChain' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY words as parameter.
#
def longestChain(words):
    # Write your code here
    dp = dict()
    words = sorted(words, key = len)
        
    for word in words: 
        max_length = 0
        for i in range(len(word)):
            predecessor = word[:i] + word[i+1:]       
            max_length = max(max_length, dp.get(predecessor, 0) + 1)
        dp[word] = max_length
    return max(dp.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    words_count = int(input().strip())

    words = []

    for _ in range(words_count):
        words_item = input()
        words.append(words_item)

    result = longestChain(words)

    fptr.write(str(result) + '\n')

    fptr.close()

# https://yjam.tistory.com/21
# https://leetcode.com/problems/longest-string-chain/discuss/428354/Python-2-Approaches%3A-DFS-%2B-Memo-DP-with-complexity-analysis