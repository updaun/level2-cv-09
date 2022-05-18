# source: https://programmers.co.kr/learn/courses/30/lessons/43165

answer = 0

def DFS(idx, numbers, target, value):
    global answer

    if idx == len(numbers):
        if target == value:
            answer += 1
        return
        
    DFS(idx+1, numbers, target, value+numbers[idx])
    DFS(idx+1, numbers, target, value-numbers[idx])
    
def solution(numbers, target):
    
    DFS(0, numbers, target, 0)
    
    return answer