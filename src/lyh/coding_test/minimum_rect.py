# programmers
# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    
    max_1, max_2 = 0, 0
    for i in range(len(sizes)):
        if sizes[i][0] > max_1:
            max_1 = sizes[i][0]
        if sizes[i][1] > max_2:
            max_2 = sizes[i][1]
            
    return max_1 * max_2