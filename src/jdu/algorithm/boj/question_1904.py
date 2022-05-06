import sys
n = int(sys.stdin.readline())

memo = [0] * 1000001

memo[1] = 1
memo[2] = 2

for i in range(3, n+1):
    memo[i] = (memo[i-1] + memo[i-2])%15746

print(memo[n])

'''
# 런타임 에러 (RecursionError)
import sys
n = int(sys.stdin.readline())

memo = dict()

def dp(n):
    if n in memo: return memo[n]
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        temp = dp(n-1) + dp(n-2)
        memo[n] = temp
        return temp

print(dp(n)%15746)
'''

'''
# 메모리 초과(배열에 너무 큰 수를 저장)
import sys
n = int(sys.stdin.readline())

memo = [0] * 1000001

memo[1] = 1
memo[2] = 2

for i in range(3, n+1):
    memo[i] = memo[i-1] + memo[i-2]

print(memo[n]%15746)
'''