# 프로그래머스, 탐욕법
# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = 0
    for x in reserve:
        if x in lost:
            lost.remove(x)
            continue
        if x-1 in lost:
            lost.remove(x-1)
            continue
        if x+1 in lost:
            lost.remove(x+1)
    
    answer = n - len(lost)
    return answer