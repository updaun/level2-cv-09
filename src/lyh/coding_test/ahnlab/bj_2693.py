import sys
from heapq import heappush, heappop


def solution(arr):
    sorted_list = list()

    for num in arr:
        heappush(sorted_list, (-num, num))
    
    for _ in range(2):
        heappop(sorted_list)
    print(heappop(sorted_list)[1])


arr = list()
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(N):
    solution(arr[i])