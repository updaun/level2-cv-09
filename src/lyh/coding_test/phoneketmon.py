# 프로그래머스, 폰켓몬
# https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    max_len = len(nums)//2
    able_len = len(set(nums))
    
    if able_len > max_len:
        return max_len
    return able_len