# programmers vowel dictionary
# https://school.programmers.co.kr/learn/courses/30/lessons/84512

from itertools import *

def solution(word):
    answer = 0
    words = list()
    
    for i in range(5):
        for item in product(['A', 'E', 'I', 'O', 'U'], repeat = i + 1):
            words.append(''.join(item))
    
    words.sort()
    return words.index(word) + 1