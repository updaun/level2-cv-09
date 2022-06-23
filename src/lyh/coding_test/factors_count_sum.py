# 프로그래머스, 약수의 개수와 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/77884

def count_factors(num):
    factors = []
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
    return len(factors)%2

def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        answer += i*(-1)**count_factors(i)
    return answer