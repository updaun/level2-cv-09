import sys
n = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())
print(target.count(v))