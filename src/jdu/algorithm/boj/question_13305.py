import sys
n = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
oil_price = list(map(int, sys.stdin.readline().split()))
cost = 0   
start = 0
temp = 1
while True:
    if start == n-1:
        break
    if start+temp > n-1:
        cost += oil_price[start] * sum(distance[start:start+temp])
        break

    if oil_price[start] <= oil_price[start+temp]:
        temp += 1
    else:
        cost += oil_price[start] * sum(distance[start:start+temp])
        start += temp
        temp = 1
print(cost)
