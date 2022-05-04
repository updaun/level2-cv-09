# https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    answer = ""
    list = ['zero', 'one', 'two', 'three', 'four', 'five',
            'six', 'seven', 'eight', 'nine', 'ten']

    i = 0
    while i < len(s):
        if s[i].isdigit():
            answer += str(s[i])
            i += 1
        else:
            j = 0
            while s[i:i+j+1] not in list:
                j += 1
            answer += str(list.index(s[i:i+j+1]))
            i += j + 1
    answer = int(answer)
    return answer