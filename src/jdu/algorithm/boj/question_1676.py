# 팩토리얼 0의 개수
# https://www.acmicpc.net/problem/1676

import sys
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

n = str(factorial(int(sys.stdin.readline())))[::-1]
result = 0 
for i in n:
    if i == "0":
        result += 1
    else:
        break
print(result)

# 더 효율적인 풀이 방법 : 규칙 찾기
'''
import sys
n = int(sys.stdin.readline())
count = 0
while n != 0:
    n //= 5
    count += n
print(count)
'''