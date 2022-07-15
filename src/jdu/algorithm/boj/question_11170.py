import sys
input = sys.stdin.readline
memo = []
temp = 0
for i in range(1000001):
    temp += str(i).count("0")
    memo.append(temp)
for i in range(int(input())):
    start, end = list(map(int, input().split()))
    if start == 0:
        print(memo[end])
    else:
        print(memo[end]-memo[start-1])
