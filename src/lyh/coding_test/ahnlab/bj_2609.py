import sys


def solution(N1, N2):
    small = min(N1, N2)
    for i in range(1, small+1):
        if ((N1 % i == 0) and (N2 % i == 0)):
            gcd = i

    lcm = int(N1 * N2 / gcd)
    print(gcd, lcm)


N1, N2 = map(int, sys.stdin.readline().rstrip().split())
solution(N1, N2)