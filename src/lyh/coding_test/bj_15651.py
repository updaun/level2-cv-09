import sys

def permutations(arr, n):
    result = []

    if n == 0:
        return [[]]

    for elem in arr: 
        for P in permutations(arr, n-1):
            result += [[elem]+P]

    return result


# 1 ~ N, M
N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [x+1 for x in range(N)]
for permutation in permutations(arr, M):
    print(' '.join(map(str, permutation)))