# source: https://www.acmicpc.net/problem/15650

'''
자연수 N, M.
- 1부터 N까지 중복 없이 M개를 고른 수열
- 오름차순
'''

n, m = list(map(int, input().split()))

s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str,s)))
        return

    for i in range(1, n+1):
        if not s or s[-1] < i:
            s.append(i)
            dfs()
            s.pop()

dfs()
