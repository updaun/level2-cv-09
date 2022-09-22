# 프로그래머스, 문열 압축
# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def get_compressed_len(length, s):
    return_len = 0
    temp_token = ""
    
    temp_len = length
    for i, _ in enumerate(s[::length]):
        loop_token = s[length * i: length * i + length]
        
        if temp_token != loop_token:
            if i != 0:
                if temp_len // length > 1:
                    return_len += len(temp_token) + len(str(temp_len // length))
                if temp_len // length == 1:
                    return_len += len(temp_token)
            temp_len = 0
            temp_token = loop_token
        temp_len += len(loop_token)
    
    if temp_len:
        if temp_len // length > 1:
            return_len += length + len(str(temp_len // length))
        else:
            return_len += temp_len
        
    return return_len

def solution(s):
    max_token_len = len(s) // 2
    min_len = len(s)
    
    for length in range(1, max_token_len + 1):
        min_len = min(min_len, get_compressed_len(length, s))
    
    return min_len

#"aabbaccc"	7
#"ababcdcdababcdcd"	9
#"abcabcdede"	8
#"abcabcabcabcdededededede"	14
#"xababcdcdababcdcd"	17