import sys
input = sys.stdin.readline
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZA'
for i in range(int(input())):
    result = ''
    for s in input().rstrip():
        result += alphabet[alphabet.index(s)+1]
    print(f"String #{i+1}")
    print(result+"\n")