import sys
while True:
    A, B, C = map(int, sys.stdin.readline().split())
    if (A,B,C) == (0,0,0):
        break
    if B-A == C-B:
        print(f"AP {int(C+(B-A))}")
    else:
        print(f"GP {int(C*(C/B))}")
    