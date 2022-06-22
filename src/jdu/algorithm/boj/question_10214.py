import sys
n = int(sys.stdin.readline())
for i in range(n):
    y, k = 0, 0
    for _ in range(9):
        a, b = list(map(int, sys.stdin.readline().split()))
        y += a
        k += b
    if y > k:
        print("Yonsei")
    elif y == k:
        print("Draw")
    else:
        print("Korea")