# 프로그래머스, 숫자 문자열과 영단어
# https://programmers.co.kr/learn/courses/30/lessons/81301

digit_dict3 = {
    'one' : '1',
    'two' : '2',
    'six' : '6'
}

digit_dict4 = {
    'zero' : '0',
    'four' : '4',
    'five' : '5',
    'nine' : '9'
}

digit_dict5 = {
    'three' : '3',
    'seven' : '7',
    'eight' : '8'
}

def solution(s):
    answer = ''
    pos = 0
    
    while pos < len(s):
        if s[pos].isdigit():
            answer += s[pos]
            pos += 1
            continue
        
        if s[pos:pos+3] in digit_dict3:
            answer += digit_dict3[s[pos:pos+3]]
            pos += 3
            continue

        if s[pos:pos+4] in digit_dict4:
            answer += digit_dict4[s[pos:pos+4]]
            pos += 4
            continue
            
        answer += digit_dict5[s[pos:pos+5]]
        pos += 5
    
    return int(answer)