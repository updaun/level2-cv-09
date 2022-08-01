import sys
import heapq

input = sys.stdin.readline
heap = []
for i in range(int(input())):
    cmd = int(input())
    if cmd == 0:
        if heap:
            print((-1)*heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, (-1)*cmd)

# import sys
# input = sys.stdin.readline
# max_heap = []
# for i in range(int(input())):
#     input_num = int(input())
#     if input_num:
#         max_heap.append(input_num)
#     else:
#         if len(max_heap) == 0:
#             print(0)
#         else:
#             target = max(max_heap)
#             print(target)
#             max_heap.remove(target)

