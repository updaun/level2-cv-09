# combination 3 num, solve primenum count

import math
from itertools import *

def is_prime_num(n):
    for i in range(2, int(math.sqrt(n))+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False

    return True

def solution(nums):
    answer = 0
    for num in combinations(nums, 3):
        answer += is_prime_num(sum(nums))
    
    return answer