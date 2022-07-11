# 프로그래머스, 문열 압축
# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def get_compressed_len(s, token_len):
    compressed_len = 0
    token_count = len(s) // token_len
    
    token_list = [s[i*token_len:(i+1)*token_len] for i in range(token_count)]    
    if token_count*token_len < len(s):
        token_list.append(s[token_count*token_len:])
    
    temp, count = token_list[0], 1
    for token in token_list[1:]:
        if temp == token:
            count += 1
        else:
            if count > 1:
                compressed_len += len(temp) + len(str(count))
            else:
                compressed_len += len(temp)
            temp = token
            count = 1
    if count > 1:
        compressed_len += len(temp) + len(str(count))
    else:
        compressed_len += len(temp)

    return compressed_len
        
def solution(s):
    max_token_len = len(s) // 2
    min_len = len(s)
    
    for token_len in range(1, max_token_len + 1):
        min_len = min(min_len, get_compressed_len(s, token_len))
    
    return min_len

#"aabbaccc"	7
#"ababcdcdababcdcd"	9
#"abcabcdede"	8
#"abcabcabcabcdededededede"	14
#"xababcdcdababcdcd"	17