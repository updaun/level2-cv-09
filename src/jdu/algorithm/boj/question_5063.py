import sys
n = int(sys.stdin.readline())
for i in range(n):
    r, e, c = list(map(int, sys.stdin.readline().split()))
    if r < e-c:
        print("advertise")
    elif r == e-c:
        print("does not matter")
    else:
        print("do not advertise")