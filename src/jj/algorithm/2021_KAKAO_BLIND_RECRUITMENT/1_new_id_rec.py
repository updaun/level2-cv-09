# source: https://programmers.co.kr/learn/courses/30/lessons/72410

'''
아이디 규칙
- 3~15자
- 알파벳 소문자, 숫자, -, _, . (.은 처음과 끝에 사용 x. 연속 사용 x)
'''

'''
1. 대문자에 대응되는 소문자 치환
2. 알파벳 소문자, 숫자, -, _, .를 제외한 모든 문자 제거
3. . 2번 이상 연속되면 하나의 .으로 치환
4. .이 처음이나 마지막에 위치하면 제거
5. 빈 문자열이면, a 대입.
6. 16자 이상이면, 첫 15개의 문자만. 제거 후 .이 끝에 위치한다면 . 제거
7. 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복.
'''

import re

def solution(new_id):
    
    # 1 - 소문자 치환
    answer = new_id.lower()
    
    # 2 - 허용된 문자(알파벳 소문자, 숫자, -, _, .) 제외 제거
    reg_exp = re.compile('[a-z0-9-_\.]')
    allowed_chars = reg_exp.findall(answer)
    answer = ''.join(allowed_chars)
    
    # 3 - 연속되는 마침표 1개로 치환.
    reg_exp = re.compile('\.{2,}')
    
    while reg_exp.search(answer):
        consecutive_period = reg_exp.search(answer)
        idx = consecutive_period.span()
        
        answer = answer[:idx[0]+1] + answer[idx[1]:]
    
    # 4 - 처음/끝에 있는 . 제거
    if answer and answer[0] == '.':
        answer = answer[1:]
        
    if answer and answer[-1] == '.':
        answer = answer[:-1]
        
    # 5 - 빈 문자열이면, a 대입
    if not answer:
        answer += 'a'
        
    # 6 - 16자 이상이면, 첫 15개의 문자만. 제거 후 .이 끝에 위치한다면 . 제거
    
    if len(answer) > 15:
        answer = answer[:15]
        
    if answer and answer[-1] == '.':
        answer = answer[:-1]
        
    # 7 - 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복.
    if len(answer) < 3:
        
        for _ in range(3-len(answer)):
            answer += answer[-1]
            
    return answer