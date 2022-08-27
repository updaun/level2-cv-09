# 소수
# https://www.acmicpc.net/problem/2581
import sys


def is_prime_number(num):
    for x in range(2, int(num**(1/2))+1):
        if not num % x:
            return False
    return True


def solution(M, N):
    flag = True
    prime_sum, prime_min = 0, 0
    for num in range(M, N+1):
        if num == 1:
            continue
        if is_prime_number(num):
            prime_sum += num
            if flag:
                prime_min = num
                flag = False

    if not flag:
        print(prime_sum)
        print(prime_min)
    else:
        print(-1)


M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())
solution(M, N)