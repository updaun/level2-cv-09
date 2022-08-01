import sys
import heapq
input = sys.stdin.readline
heap = []
for i in range(int(input())):
    cmd = int(input())
    if cmd == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, cmd)