#https://programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    answer = []
    lenm = len(msg)
    dictionary = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
    dictionary = dictionary.split()
    if len(msg) == 1: return [dictionary.index(msg) + 1]
    while msg:
        m = msg[0]
        i = 1
        while m in dictionary:
            i += 1
            new = m
            
            
            m = msg[:i]
            if m not in dictionary:
                answer.append(dictionary.index(new)+1)
                dictionary.append(m)
                break
            if i == lenm:
                answer.append(dictionary.index(new)+1)
                break
        msg = msg[i-1:]
        
    return answer