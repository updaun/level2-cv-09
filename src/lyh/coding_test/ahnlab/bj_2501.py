import sys


def solution(N, K):
    nth = 0
    for i in range(1, N+1):
        if not N % i:
            nth += 1
            if nth == K:
                return i
    return 0


N, K = map(int, sys.stdin.readline().rstrip().split())
print(solution(N, K))