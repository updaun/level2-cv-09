# https://programmers.co.kr/learn/courses/30/lessons/17687

def convert_notation(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)

    return convert_notation(q, base) + T[r] if q else T[r]

def solution(n, t, m, p):
    answer = ''
    total = t*m
    result = ''
    for i in range(total):
        num = convert_notation(i, n)
        result += str(num) 
    
    for j in range(t):
        time = p + m*(j)
        answer += result[time-1]
        
    return answer