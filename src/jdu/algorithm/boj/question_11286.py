import sys
import heapq
input = sys.stdin.readline
h = []
for i in range(int(input())):
    n = int(input())
    if n == 0:
        if len(h) == 0:
            print(0)
        else:
            print(heapq.heappop(h)[1])
    else:
        heapq.heappush(h, (abs(n),n))
    