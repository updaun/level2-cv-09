import sys
import heapq
input = sys.stdin.readline
n = int(input())
cards = []
for i in range(n):
    heapq.heappush(cards, int(input()))
if len(cards) == 1:
    print(0)
else:
    result = 0
    while len(cards) > 1:
        a = heapq.heappop(cards)
        b = heapq.heappop(cards)
        result += (a+b)
        heapq.heappush(cards, a+b)
print(result)

# 시간 초과
# import sys
# input = sys.stdin.readline
# n = int(input())
# cards = []
# for i in range(n):
#     cards.append(int(input()))
# target = sorted(cards)
# if n == 1:
#     result = target[0]
# else:
#     result = 0
#     for i in range(1, n):
#         result += sum(target[:i+1])    
# print(result)