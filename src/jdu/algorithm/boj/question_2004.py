import sys
n, k = list(map(int, sys.stdin.readline().split()))

def count_two(n):
    count = 0 
    while n != 0:
        n //= 2
        count += n
    return count

def count_five(n):
    count = 0
    while n != 0:
        n //= 5
        count += n
    return count

print(min(count_two(n)-count_two(n-k)-count_two(k), count_five(n)-count_five(n-k)-count_five(k)))

# 시간 초과
'''
import sys
from math import factorial
n, k = list(map(int, sys.stdin.readline().split()))

def bino_coef(n, k):
    return int(factorial(n)/factorial(k)/factorial(n-k))

n_str = str(bino_coef(n,k))
count = 0
for i in n_str[::-1]:
    if i == "0":
        count+=1
    else:
        break
print(count)
'''

# 메모리 초과
'''
import sys
n, k = list(map(int, sys.stdin.readline().split()))

def bino_coef(n, r):
    cache = [[0 for _ in range(r+1)] for _ in range(n+1)]
    for i in range(n+1):
        cache[i][0] = 1
    
    for i in range(r+1):
        cache[i][i] = 1
    
    for i in range(1, n+1):
        for j in range(1, r+1):
            cache[i][j] = cache[i-1][j] + cache[i-1][j-1]
    return cache[n][r]

n_str = str(bino_coef(n,k))
count = 0
for i in n_str[::-1]:
    if i == "0":
        count+=1
    else:
        break
print(count)

'''