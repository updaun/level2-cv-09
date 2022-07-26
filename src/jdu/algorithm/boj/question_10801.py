import sys
input = sys.stdin.readline
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_point = 0
B_point = 0
for i in range(10):
    if A[i] > B[i]:
        A_point += 1
    elif B[i] > A[i]:
        B_point += 1
if A_point > B_point:
    print('A')
elif A_point == B_point:
    print('D')
else:
    print('B')
