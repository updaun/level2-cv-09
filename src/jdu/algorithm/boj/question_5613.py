import sys
input = sys.stdin.readline
result = int(input())
cmd = ''
while True:
    s = input().rstrip()
    if s == "=":
        break
    if s.isdigit():
        if cmd == '+':
            result += int(s)
        elif cmd == '-':
            result -= int(s)
        elif cmd == '*':
            result *= int(s)
        else:
            result //= int(s)
    else:
        cmd = s
print(int(result))
