# https://programmers.co.kr/learn/courses/30/lessons/42842

def getMyDivisor(n):
    # https://minnit-develop.tistory.com/16

    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)

    divisorsList.sort()
    
    return divisorsList

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    div_list = getMyDivisor(yellow)
    
    for div in div_list:
        x_yellow = div
        y_yellow = yellow/div
    
        if (x_yellow + 2) * 2 + y_yellow * 2 == brown:
            return [y_yellow + 2, x_yellow + 2]
    
    return answer