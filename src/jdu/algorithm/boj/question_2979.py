import sys
input = sys.stdin.readline
price = list(map(int, input().split()))
temp = [0]*101
result = 0
for i in range(3):
    s, f = map(int, input().split())
    for j in range(s, f):
        temp[j] += 1
for c in temp:
    if c != 0:
        result += price[c-1]*c
print(result)