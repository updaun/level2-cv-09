import sys
input = sys.stdin.readline
while True:
    j, m = map(int, input().split())
    if j == 0 and m == 0:
        break
    a, b = divmod(j, m)
    print(f'{a} {b} / {m}')