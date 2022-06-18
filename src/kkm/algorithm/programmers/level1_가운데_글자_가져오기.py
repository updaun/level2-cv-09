# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    answer = ''
    if len(s)%2 == 0:
        return s[int(len(s)/2)-1] + s[int(len(s)/2)]
    else:
        return s[len(s)//2]
    return answer