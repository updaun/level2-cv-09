# source: https://www.acmicpc.net/problem/1463

'''
정수 X에 사용할 수 있는 연산
1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다

정수 N이 주어졌을 때, 위 연산 3개를 적절히 이용해서 1을 만드려고 한다.
연산 사용 횟수 최솟값을 출력.

1 <= N <= 10^6
'''

n = int(input())

memo = [int(1e6)] * (n+1)
memo[1] = 0

for i in range(1, n+1):
    if i * 2 <= n and memo[i] + 1 < memo[i*2]: memo[i*2] = memo[i] + 1

    if i * 3 <= n and memo[i] + 1 < memo[i*3]: memo[i*3] = memo[i] + 1

    if i < n and memo[i] + 1 < memo[i+1]: memo[i+1] = memo[i] + 1

print(memo[n])