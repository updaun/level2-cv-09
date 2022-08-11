import sys
input = sys.stdin.readline
for i in range(int(input())):
    n, d = map(int, input().split())
    count = 0
    for i in range(n):
        v, f, c = map(int, input().split())
        if d <= v/c*f:
            count += 1
    print(count)
