import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    stores = list(map(int, input().split()))
    stores = sorted(stores, reverse=True)
    stores.append(stores[0])
    result = 0
    for j in range(1, n+1):
        result += abs(stores[j]-stores[j-1])
    print(result)