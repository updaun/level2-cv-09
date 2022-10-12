# python find prime_number
# https://school.programmers.co.kr/learn/courses/30/lessons/42839

import math
from itertools import *

def is_prime_number(number):
    if number < 2:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if not number % i:
            return False
    return True

def solution(numbers):
    answer = 0
    numbers_count = len(numbers)
    numbers = list(numbers)
    
    number_list = list()
    for i in range(1, numbers_count + 1):
        for nums in permutations(numbers, i):
            number_list.append(int(''.join(nums)))
    
    for number in set(number_list):
        answer += is_prime_number(number)
    
    return answer