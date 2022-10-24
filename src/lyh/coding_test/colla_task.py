# programmers level1 task
# https://school.programmers.co.kr/learn/courses/30/lessons/132267

def solution(a, b, n):
    answer = 0
    
    while n >= a:
        share, rest = n // a, n % a
        answer += share * b
        n = share * b + rest
    
    return answer