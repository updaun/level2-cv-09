# https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    answer = 0
    start = min(a,b)
    end = max(a,b)
    if start == end: return start
    for i in range(start, end + 1):
        answer += i
    return answer