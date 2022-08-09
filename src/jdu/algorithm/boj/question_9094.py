import sys
def solution():
    ret = 0
    for a in range(1, n):
        for b in range(a + 1, n):
            if memo[a][b][m] != -1:
                ret += memo[a][b][m]
                continue
            numerator, denominator = (a**2 + b**2 + m), (a * b)
            if numerator % denominator == 0:
                ret += 1
                memo[a][b][m] = 1
            else:
                memo[a][b][m] = 0
    return ret

if __name__ == '__main__':
    T = int(input())
    memo = [[[-1 for _ in range(101)] for _ in range(101)] for _ in range(101)]
    for _ in range(T):
        n, m = list(map(int, sys.stdin.readline().split()))
        answer = solution()
        print(answer)

# 시간 초과
# import sys
# from itertools import combinations
# input = sys.stdin.readline
# for _ in range(int(input())):
#     n, m = map(int, input().split())
#     print(sum([(a**2+b**2+m) % (a*b) == 0 for a,b in combinations(range(1,n), 2)]))


# 시간 초과
# import sys
# input = sys.stdin.readline
# for i in range(int(input())):
#     n, m = map(int, input().split())
#     count = 0
#     for a in range(1, n-1):
#         for b in range(a+1, n):
#             if (a**2+b**2+m) % (a*b) == 0:
#                 count += 1
#     print(count)