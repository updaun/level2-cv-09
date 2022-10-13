# carpet task
# https://school.programmers.co.kr/learn/courses/30/lessons/42842

import math

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    h = int(math.sqrt(total))
    
    while h > 0:
        if (total / h) % 1 == 0:
            w = total / h
            if w >= h:
                if 2 * w + 2 * h == 4 + brown:
                    return [w, h]
        h -= 1
    
    return answer