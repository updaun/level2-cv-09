import sys
n = int(sys.stdin.readline())
q_list = []
for _ in range(n):
    x1, y1, x2, y2 = list(map(int, sys.stdin.readline().split()))
    k = int(sys.stdin.readline())
    count = 0
    for _ in range(k):
        cx, cy, r = list(map(int, sys.stdin.readline().split()))
        if ((cx-x1)**2 + (cy-y1)**2)**0.5 < r and ((cx-x2)**2 + (cy-y2)**2)**0.5 < r:
            continue
        elif ((cx-x1)**2 + (cy-y1)**2)**0.5 < r or ((cx-x2)**2 + (cy-y2)**2)**0.5 < r:
            count += 1
    print(count)    