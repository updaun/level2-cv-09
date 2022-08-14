# source: https://www.acmicpc.net/problem/9663

'''
N x N 체스판.
퀸 N개를 서로 공격할 수 없도록.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하기.

1 <= N < 15

시간 제한: 10초
메모리 제한: 128MB
'''

n = int(input())

col = set()
posDiag = set() # (r + c)
negDiag = set() # (r - c)

ans = 0

def backtrack(r):
    if r == n:

        global ans

        ans += 1
                
        return
            
    for c in range(n):
        if c in col or (r + c) in posDiag or (r - c) in negDiag:
            continue
                
        col.add(c)
        posDiag.add(r + c)
        negDiag.add(r - c)
                
        backtrack(r + 1)
                
        col.remove(c)
        posDiag.remove(r + c)
        negDiag.remove(r - c)

backtrack(0)

print(ans)