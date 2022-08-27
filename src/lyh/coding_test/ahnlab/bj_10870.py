import sys

def solution(n):
    F_n = [0, 1]
    if n < 2:
        print(F_n[n])
        return
    
    for _ in range(n-1):
        F_n.append(F_n[-1] + F_n[-2])
    print(F_n[-1])


n = int(sys.stdin.readline().rstrip())
solution(n)