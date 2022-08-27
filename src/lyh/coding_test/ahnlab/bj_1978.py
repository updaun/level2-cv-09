import sys


def is_prime_number(num):
    for i in range(2, int(num**(1/2))+1):
        if not num % i:
            return False

    return True


def solution(arr):
    prime_cnt = 0

    for num in arr:
        if num == 1:
            continue
        prime_cnt += is_prime_number(num)
    
    print(prime_cnt)


N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

solution(arr)