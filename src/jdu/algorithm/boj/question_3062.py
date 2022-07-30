import sys
input = sys.stdin.readline
for i in range(int(input())):
    A = input().rstrip()
    B = A[::-1]
    C = str(int(A) + int(B))
    mid_idx = int(len(C)/2)
    if len(C)%2 == 0:
        if C[:mid_idx+1] == C[mid_idx-1:][::-1]:
            print('YES')
        else:
            print('NO')
    else:
        if C[:mid_idx+1] == C[mid_idx:][::-1]:
            print('YES')
        else:
            print('NO')
