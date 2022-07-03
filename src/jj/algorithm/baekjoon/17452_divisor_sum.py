# source: https://www.acmicpc.net/problem/17425
# ref: https://earthconquest.tistory.com/370

'''
두 자연수 A와 B가 있을 때, A = BC를 만족하는 자연수 C를 A의 약수라고 한다. 
예를 들어, 2의 약수는 1, 2가 있고, 24의 약수는 1, 2, 3, 4, 6, 8, 12, 24가 있다. 
자연수 A의 약수의 합은 A의 모든 약수를 더한 값이고, f(A)로 표현한다. 
x보다 작거나 같은 모든 자연수 y의 f(y)값을 더한 값은 g(x)로 표현한다.

자연수 N이 주어졌을 때, g(N)을 구해보자.
'''

'''
f(A): A 약수의 합
g(x): x 보다 작거나 같은 f(y)들의 합.
'''

'''
입력
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 100,000)가 주어진다. 둘째 줄부터 테스트 케이스가 한 줄에 하나씩 주어지며 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.
'''

'''
출력
각각의 테스트 케이스마다, 한 줄에 하나씩 g(N)를 출력한다.
'''

# pypy3로 해야 시간 초과 안 남.

# dynamic programming
from sys import stdin

input = stdin.readline

f = [1] * 1000001 # 모든 자연수는 1을 약수로 가지므로, 모든 원소 1로 초기화.
g = [0] * 1000001

# i의 배수는 i를 약수로 가지므로, i를 더해준다.
for i in range(2, len(f)):
    j = 1
    while i*j < len(f):
        f[i*j] += i
        j += 1

for i in range(1, len(g)):
    g[i] = g[i-1] + f[i]

n = int(input())

for _ in range(n):
    x = int(input())
    print(g[x])