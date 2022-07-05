# 프로그래머스, 내적
# https://school.programmers.co.kr/learn/courses/30/lessons/70128

def dot_projection(a, b):
    sumation = 0
    for num_a, num_b in zip(a, b):
        sumation += num_a * num_b
    return sumation

def solution(a, b):
    answer = 1234567890
    answer = dot_projection(a, b)

    return answer