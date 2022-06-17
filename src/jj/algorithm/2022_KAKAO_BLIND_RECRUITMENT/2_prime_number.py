# source: https://programmers.co.kr/learn/courses/30/lessons/92335

import math

def solution(n, k):
    
    answer = 0
    
    converted = []
    
    while n:
        converted.append(str(n % k))
        
        n //= k
    
    converted.reverse()
    
    converted_str = ''.join(converted)
    
    num_split = converted_str.split('0')
    
    for num in num_split:
        
        is_prime = True
        
        if num != '':
            num = int(num)
            
            if num == 1:
                    is_prime = False
            
            #for i in range(2, num): 시간 초과
            for i in range(2, int(math.sqrt(num)) + 1):
                
                if num % i == 0:
                    is_prime = False
            
            if is_prime:
                answer += 1
    
    return answer