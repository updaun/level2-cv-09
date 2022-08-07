import sys
input = sys.stdin.readline
N, M = map(int, input().split())
ball = dict()
for i in range(1, N+1):
    ball[i] = i
for i in range(M):
    A, B = map(int, input().split())
    CA, CB = ball[A], ball[B]
    ball[A] = CB
    ball[B] = CA
print(" ".join(map(str, [ball[i] for i in range(1, N+1)])))