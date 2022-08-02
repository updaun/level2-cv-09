import sys
input = sys.stdin.readline
memo = [1,1,2,4]
def koong(n):
    if n < len(memo):
        return memo[n]
    else:
        temp = koong(n-1) + koong(n-2) + koong(n-3) + koong(n-4) 
        memo.append(temp)
        return memo[n]
for i in range(int(input())):
    print(koong(int(input())))