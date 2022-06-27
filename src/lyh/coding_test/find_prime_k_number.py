# 프로그래머스, k진수에서 소수의 개수 구하기
# https://programmers.co.kr/learn/courses/30/lessons/92335

import math

def convert_digit(num, base):
    tmp = ''
    while num:
        tmp = str(num%base) + tmp
        num //= base
    return tmp

def primenumber(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x) + 1)):
    	if x % i == 0:
        	return False
    return True

def count_prime_number(num_list):
    tmp = 0
    for i in num_list:
        if not i: continue
        if primenumber(int(i)):
            tmp += 1
    return tmp

def solution(n, k):
    answer = -1
    
    converted_num = convert_digit(n, k)
    converted_list = converted_num.split("0")
    
    answer = count_prime_number(converted_list)
    return answer