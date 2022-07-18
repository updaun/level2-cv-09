import sys
input = sys.stdin.readline
n = int(input())
stack = []
for i in range(n):
    cmd = list(map(str, input().split()))
    if cmd[0] == 'push':
        stack.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        print(int(len(stack)==0))
    elif cmd[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
    