import sys
input = sys.stdin.readline
n = int(input())
def gcd(a,b):
    while b:
        a, b = b, a%b
    return a
for i in range(n):
    a, b = map(int, input().split())
    gcd_value = gcd(a,b)
    print((a*b)//gcd_value, gcd_value)