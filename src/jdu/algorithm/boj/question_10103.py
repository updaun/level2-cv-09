import sys
n = int(sys.stdin.readline())
c_score = 100
s_score = 100
for i in range(n):
    c, s = list(map(int, sys.stdin.readline().split()))
    if c == s:
        continue
    elif c > s:
        s_score -= c
    else:
        c_score -= s
print(c_score)
print(s_score)