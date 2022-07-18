# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def one_counter(n):
    binary = str(format(n, 'b'))
    one = 0
    for i in binary:
        if i == "1":
            one += 1
    return one
            
def solution(n):
    answer = 0
    target = one_counter(n)
    n += 1
    while one_counter(n) != target:
        n += 1
        
    return n