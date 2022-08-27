# https://www.acmicpc.net/problem/1292
# 쉽게 푸는 문제
import sys


def solution(A, B):
    idx, result = 0, 0
    for num in range(1, 51):
        for i in range(num):
            idx += 1
            if idx >= A:
                result += num
            if idx == B:
                return result
    return 0


A, B = map(int, sys.stdin.readline().rstrip().split())
print(solution(A, B))