# https://velog.io/@sloools/Python-%EC%88%9C%EC%97%B4Permutation-%EC%A1%B0%ED%95%A9Combination
# Implementation of the number of cases
import sys
from heapq import heapify, heappop


result = list()
def nCr(n, ans, r, peoples):
    global result
    if n == len(peoples):
        if len(ans) == r:
            if sum(ans) == 100:
                result = ans[:]
                return True
        return False
    ans.append(peoples[n])
    if nCr(n+1, ans, r, peoples):
        return True
    ans.pop()
    if nCr(n+1, ans, r, peoples):
        return True


def solution(peoples):
    nCr(0, [], 7, peoples)


peoples = list()
for _ in range(9):
    peoples.append(int(sys.stdin.readline().rstrip()))

solution(peoples)
heapify(result)
for _ in range(7):
    print(heappop(result))