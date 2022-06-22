import sys
target_time = int(sys.stdin.readline())
A = 0
B = 0
C = 0
while True:
    if target_time < 10:
        break
    if target_time >= 300:
        target_time -= 300
        A += 1
    elif target_time >= 60:
        target_time -= 60
        B += 1
    else:
        target_time -= 10
        C += 1
if target_time != 0:
    print(-1)
else:
    print(A,B,C)