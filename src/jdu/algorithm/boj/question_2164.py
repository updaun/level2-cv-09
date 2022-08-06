from collections import deque
n = int(input())
l = deque([i for i in range(1, n+1)])
while len(l) > 1:
    l.popleft()
    l.rotate(-1)
print(l[0])

# 시간 초과
# n = int(input())
# if n % 2 == 0:
#     l = [i for i in range(1, n+1) if i%2==0]
# else:
#     l = [n]+[i for i in range(1, n+1) if i%2==0]
# while len(l) > 2:
#     l.pop(0)
#     l = l[1:]+[l[0]]
# print(l.pop(1))
