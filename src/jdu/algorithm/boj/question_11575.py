import sys
input = sys.stdin.readline
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
crypto = dict()
recrypto = dict()
for i in range(26):
    crypto[alphabet[i]] = i
    recrypto[i] = alphabet[i]
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    result = ''
    for s in input().rstrip():
        result += recrypto[(crypto[s]*a + b)%26]
    print(result)