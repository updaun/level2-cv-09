# https://programmers.co.kr/learn/courses/30/lessons/92335

import math

# 소수 판별 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def solution(n, k):
    answer = 0
    tmp = ''
    while n:
        tmp += str(n % k)
        n = n // k
    tmp = tmp[::-1].split('0')
    for t in tmp:
        if t != '':
            if t != '1':
                if is_prime_number(int(t)):
                    answer += 1
    return answer