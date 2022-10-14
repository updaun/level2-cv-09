# programmers DFS task - target number
# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def DFS(idx, val, numbers, target):
    case_cnt = 0
    if idx == len(numbers):
        if val == target:
            return True
        return False
    
    case_cnt += DFS(idx + 1, val + numbers[idx], numbers, target)
    case_cnt += DFS(idx + 1, val - numbers[idx], numbers, target)
    return case_cnt

def solution(numbers, target):
    answer = DFS(0, 0, numbers, target)
    
    return answer