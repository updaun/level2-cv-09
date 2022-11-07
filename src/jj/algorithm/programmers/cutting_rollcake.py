# source: https://school.programmers.co.kr/learn/courses/30/lessons/132265

'''
롤 케이크를 두 조각으로 잘라서 한 조각씩 나눠 먹는다.
롤케이크에 여러 토핑이 일렬로 올려져 있다.
각 조각에 동일한 가짓수의 토핑이 올라가면 '공평하게' 롤케이크가 나누어진 것이다.
'공평하게' 자르는 방법의 수를 return. '공평하게' 나누지 못하는 경우도 있다.
'''
from collections import Counter

def solution(topping):
    answer = 0
    
    topping_count = Counter(topping)
    
    cake1 = set(topping)
    cake2 = set([])
    
    while topping:
        top = topping.pop()
        
        cake2.add(top)
        topping_count[top] -= 1
        
        if topping_count[top] < 1:
            cake1.remove(top)
        
        if len(cake1) == len(cake2):
            answer += 1
    
    return answer